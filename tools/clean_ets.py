"""Normalize imported ETS text conservatively; ETS_2023 is the reference.

Run from the repository root. Ambiguous OCR content is left for source review.
"""
from pathlib import Path
import re

QUESTION = re.compile(r"^(\d{2,3})\.\s*(?!\(\s*[A-D]\))\S")
OPTION = re.compile(r"^(?:\d{2,3}\.\s*)?\([A-D]\)")
GROUP = re.compile(r"^Questions?\s+\d", re.I)
HEADER = re.compile(r"^(?:To|From|Cc|Date|Sent|Subject|Attachments?):", re.I)
WATERMARK = re.compile(r'Nhom\s+hoc\s+\S+\s+anh\s+Toeic\s+Practice\s+Club(?:[ \t]*[,\.])?[ \t]*', re.I)
PAGE_FOOTER = re.compile(r'(?:GO|60)\s*ON\s*(?:TO|l\^)\s*THE\s*NEXT\s*PAG(?:E|\^\^)', re.I)


def clean(source):
    text = source.replace('\ufeff', '').replace('\u00a0', ' ')
    text = WATERMARK.sub('', text)
    text = re.sub(r'[ \t]+', ' ', text)
    # Separate OCR blocks that were concatenated at page boundaries.
    text = re.sub(r'(?<!\n)(READING TEST|PART [3-7]\b|Questions? \d{2,3}[-–])', r'\n\1', text)
    text = re.sub(r'(?<=[a-zA-Z).?!])(?=(?:\d{2,3})\.\s+[A-Z])', '\n', text)
    text = re.sub(r'(?m)^\d{1,3}(?=(?:PART [3-7]|Questions? \d|GO ON TO THE NEXT PAGE))', '', text)
    text = re.sub(r'(?m)^ETSREAD5NG TEST$', 'READING TEST', text)
    text = re.sub(r'(?m)^PARTS(?=\nDirections: A word or phrase)', 'PART 5', text)
    text = re.sub(r'(?m)^\s*/([A-D])\)', r'(\1)', text)
    text, removed = PAGE_FOOTER.subn('', text)
    lines = []
    for raw in text.splitlines():
        line = raw.strip()
        if re.fullmatch(r'(?:\d{1,3})?GO ON TO THE NEXT PAGE[.!]?|(?:ETS )?TEST(?:\s*\d+){0,2}|Nhom hoc tieng anh Toeic Practice Club', line):
            removed += 1
            continue
        lines.append(line)
    # Remove isolated page numbers only between a finished option and a new block.
    for i, line in enumerate(lines):
        if re.fullmatch(r'\d{1,3}', line):
            before = next((x for x in reversed(lines[:i]) if x), '')
            after = next((x for x in lines[i+1:] if x), '')
            if (OPTION.match(before) or before.endswith('answer sheet.')) and (QUESTION.match(after) or GROUP.match(after) or after.startswith('PART ')):
                lines[i] = ''
                removed += 1
    # Part 6 numbers printed underneath blanks become inline labels as in ETS2023.
    labeled = 0
    part = None
    group_start = 0
    deleted = set()
    for i, line in enumerate(lines):
        if re.fullmatch(r'PART [3-7]', line):
            part = int(line[-1])
        if GROUP.match(line):
            group_start = i
        if part == 6 and re.fullmatch(r'(?:13[1-9]|14[0-6])\.', line):
            number = line[:-1]
            candidates = []
            for j in range(group_start + 1, i):
                if OPTION.match(lines[j]):
                    continue
                for m in re.finditer(r'-{3,}', lines[j]):
                    if not re.search(r'\(\d{3}\)\s*$', lines[j][:m.start()]):
                        candidates.append((j, m.start()))
            if len(candidates) == 1:
                j, pos = candidates[0]
                lines[j] = lines[j][:pos].rstrip() + ' (' + number + ') ' + lines[j][pos:]
                deleted.add(i)
                labeled += 1
            group_start = i
    # Normalize blank widths and spacing without changing the answer text.
    lines = [re.sub(r'\s*-{3,}\s*', ' ------- ', x).strip() for i, x in enumerate(lines) if i not in deleted]
    lines = [re.sub(r'------- ([.,;:])', r'-------\1', x) for x in lines]
    result = []
    i = 0
    part = None
    while i < len(lines):
        line = lines[i]
        if re.fullmatch(r'PART [3-7]', line):
            part = int(line[-1])
        if QUESTION.match(line):
            j = i + 1
            while j < len(lines) and j-i < 12 and lines[j] and not (OPTION.match(lines[j]) or QUESTION.match(lines[j]) or GROUP.match(lines[j]) or lines[j].startswith('PART ')):
                j += 1
            if j < len(lines) and re.match(r'^\(A\)', lines[j]):
                line = ' '.join(lines[i:j])
                i = j - 1
        elif OPTION.match(line):
            j = i + 1
            while j < len(lines) and lines[j] and not (OPTION.match(lines[j]) or QUESTION.match(lines[j]) or GROUP.match(lines[j]) or HEADER.match(lines[j]) or lines[j].startswith(('PART ', 'READING TEST'))):
                # D may be followed immediately by a passage or a table: join
                # only clear lower-case continuations outside Part 5.
                if part != 5 and (re.match(r'^\(D\)', line) or re.match(r'^\d+\. \(D\)', line)):
                    if line.endswith(('.', '?', '!', ':')) or not re.match(r'^[a-z]', lines[j]):
                        break
                if part != 5 and j-i > 5:
                    break
                line += ' ' + lines[j]
                j += 1
            i = j - 1
        if GROUP.match(line):
            if result and result[-1]:
                result.append('')
            result.extend([line, ''])
        else:
            result.append(line)
        i += 1
    output = re.sub(r'\n{3,}', '\n\n', '\n'.join(result)).strip() + '\n'
    # All words and numbers survive in order, except known page furniture,
    # standard blank widths, and deliberately moved Part 6 labels.
    assert output.count('(A)') >= source.count('(A)')
    for choice in 'BCD':
        assert output.count(f'({choice})') >= source.count(f'({choice})')
    return output, removed, labeled


def main():
    rows = []
    for path in sorted(Path('.').glob('ETS_*/*/*.txt')):
        if path.parts[0] == 'ETS_2023':
            continue
        original = path.read_text()
        if not original:
            rows.append(f'| {path} | 0 | 0 | 0 | File trống |')
            continue
        output, removed, labeled = clean(original)
        for _ in range(4):
            normalized, extra_removed, extra_labeled = clean(output)
            removed += extra_removed
            labeled += extra_labeled
            if normalized == output:
                break
            output = normalized
        assert clean(output)[0] == output, path
        path.write_text(output)
        tests = len(re.findall(r'(?m)^PART 5$', output))
        notes = []
        if tests > 1:
            notes.append(f'Gộp {tests} đề; giữ vị trí file gốc')
        if not tests:
            notes.append('Không có Reading/PART 5')
        if re.search(r'(?m)^(?:To|From|Date|Subject|Cc|Attachment)\s*$', output):
            notes.append('Header mail rời cần đối chiếu')
        if re.search(r'(?m)^1[34]\d\.$', output):
            notes.append('Số chỗ trống PART 6 chưa gắn được chắc chắn')
        rows.append(f'| {path} | {tests} | {removed} | {labeled} | {"; ".join(notes) or "Đã chuẩn hóa định dạng"} |')
    report = '''# Làm sạch các bộ ETS mới

ETS2023 là mẫu tham chiếu và được giữ nguyên. Công cụ: `python3 tools/clean_ets.py`.

Đã thống nhất UTF-8/LF, khoảng trắng và độ dài dấu trống; tách tiêu đề/số câu bị dính; nối câu hỏi và lựa chọn xuống dòng; bỏ footer chuyển trang và nhãn TEST; chuyển số dưới chỗ trống PART 6 thành `(131) -------` khi xác định duy nhất một vị trí; tách nhóm bài bằng dòng trống.

Không tự bổ sung câu, đáp án, thông tin mail hoặc sửa từ tiếng Anh chưa có căn cứ. Giữ file gộp tại vị trí cũ vì chưa đủ bằng chứng về mã đề/phiên bản để tách và đánh số lại an toàn. Số đề dưới đây được đếm theo PART 5.

| File | Số đề Reading | Dòng thừa bỏ | Chỗ trống gắn số | Ghi chú |
| --- | ---: | ---: | ---: | --- |
''' + '\n'.join(rows) + '''

## Cần đối chiếu nguồn

- ETS2024/TEST5 trống; ETS2025/TEST1 chỉ có câu 32–100, không có transcript và Reading.
- Các năm 2018–2022 có nhiều đề gộp trong một file. Không coi tên thư mục TEST1 hiện tại là bằng chứng file chỉ chứa một đề.
- OCR hai cột có thể xen câu hỏi và lựa chọn (ví dụ ETS2019, đề thứ ba, câu 101/105); cần PDF/ảnh gốc để khôi phục thứ tự chính xác.
- Bảng, lịch, hội thoại, địa chỉ và phần thân bài đọc được giữ xuống dòng để tránh ghép sai cấu trúc.
- Header mail bị mất nhãn hoặc xáo trộn, chữ sai OCR, hình minh họa và chỗ trống bị mất nét chưa thể xác nhận chỉ từ TXT. Không suy đoán để lấp dữ liệu thiếu.
'''
    Path('ETS_CLEANUP_REVIEW.md').write_text(report)


if __name__ == '__main__':
    main()
