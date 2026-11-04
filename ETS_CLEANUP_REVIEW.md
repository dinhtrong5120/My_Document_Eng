# Làm sạch các bộ ETS mới

ETS2023 là mẫu tham chiếu và được giữ nguyên. Công cụ: `python3 tools/clean_ets.py`.

Đã thống nhất UTF-8/LF, khoảng trắng và độ dài dấu trống; tách tiêu đề/số câu bị dính; nối câu hỏi và lựa chọn xuống dòng; bỏ footer chuyển trang và nhãn TEST; chuyển số dưới chỗ trống PART 6 thành `(131) -------` khi xác định duy nhất một vị trí; tách nhóm bài bằng dòng trống.

Không tự bổ sung câu, đáp án, thông tin mail hoặc sửa từ tiếng Anh chưa có căn cứ. Giữ file gộp tại vị trí cũ vì chưa đủ bằng chứng về mã đề/phiên bản để tách và đánh số lại an toàn. Số đề dưới đây được đếm theo PART 5.

| File | Số đề Reading | Dòng thừa bỏ | Chỗ trống gắn số | Ghi chú |
| --- | ---: | ---: | ---: | --- |
| ETS_2018/TEST1/ETS2018.txt | 5 | 247 | 10 | Gộp 5 đề; giữ vị trí file gốc; Header mail rời cần đối chiếu; Số chỗ trống PART 6 chưa gắn được chắc chắn |
| ETS_2018/TEST2/ETS2018.txt | 5 | 150 | 5 | Gộp 5 đề; giữ vị trí file gốc; Số chỗ trống PART 6 chưa gắn được chắc chắn |
| ETS_2018/TEST3/ETS2018.txt | 1 | 4 | 0 | Số chỗ trống PART 6 chưa gắn được chắc chắn |
| ETS_2019/TEST1/ETS2019.txt | 10 | 320 | 34 | Gộp 10 đề; giữ vị trí file gốc; Header mail rời cần đối chiếu; Số chỗ trống PART 6 chưa gắn được chắc chắn |
| ETS_2020/TEST1/ETS2020.txt | 10 | 386 | 39 | Gộp 10 đề; giữ vị trí file gốc; Số chỗ trống PART 6 chưa gắn được chắc chắn |
| ETS_2021/TEST1/ETS2021.txt | 5 | 147 | 15 | Gộp 5 đề; giữ vị trí file gốc; Số chỗ trống PART 6 chưa gắn được chắc chắn |
| ETS_2022/TEST1/ETS2022.txt | 10 | 393 | 35 | Gộp 10 đề; giữ vị trí file gốc; Số chỗ trống PART 6 chưa gắn được chắc chắn |
| ETS_2024/TEST1/ETS2024.txt | 1 | 44 | 14 | Số chỗ trống PART 6 chưa gắn được chắc chắn |
| ETS_2024/TEST10/ETS2024.txt | 1 | 33 | 10 | Số chỗ trống PART 6 chưa gắn được chắc chắn |
| ETS_2024/TEST2/ETS2024.txt | 1 | 7 | 6 | Số chỗ trống PART 6 chưa gắn được chắc chắn |
| ETS_2024/TEST3/ETS2024.txt | 1 | 38 | 14 | Số chỗ trống PART 6 chưa gắn được chắc chắn |
| ETS_2024/TEST4/ETS2024.txt | 1 | 41 | 5 | Số chỗ trống PART 6 chưa gắn được chắc chắn |
| ETS_2024/TEST5/ETS2024.txt | 0 | 0 | 0 | File trống |
| ETS_2024/TEST6/ETS2024.txt | 1 | 42 | 9 | Số chỗ trống PART 6 chưa gắn được chắc chắn |
| ETS_2024/TEST7/ETS2024.txt | 1 | 33 | 4 | Số chỗ trống PART 6 chưa gắn được chắc chắn |
| ETS_2024/TEST8/ETS2024.txt | 1 | 40 | 4 | Số chỗ trống PART 6 chưa gắn được chắc chắn |
| ETS_2024/TEST9/ETS2024.txt | 1 | 43 | 8 | Số chỗ trống PART 6 chưa gắn được chắc chắn |
| ETS_2025/TEST1/ETS2025.txt | 0 | 0 | 0 | Không có Reading/PART 5 |

## Cần đối chiếu nguồn

- ETS2024/TEST5 trống; ETS2025/TEST1 chỉ có câu 32–100, không có transcript và Reading.
- Các năm 2018–2022 có nhiều đề gộp trong một file. Không coi tên thư mục TEST1 hiện tại là bằng chứng file chỉ chứa một đề.
- OCR hai cột có thể xen câu hỏi và lựa chọn (ví dụ ETS2019, đề thứ ba, câu 101/105); cần PDF/ảnh gốc để khôi phục thứ tự chính xác.
- Bảng, lịch, hội thoại, địa chỉ và phần thân bài đọc được giữ xuống dòng để tránh ghép sai cấu trúc.
- Header mail bị mất nhãn hoặc xáo trộn, chữ sai OCR, hình minh họa và chỗ trống bị mất nét chưa thể xác nhận chỉ từ TXT. Không suy đoán để lấp dữ liệu thiếu.

## Rà soát đáp án hai cột

Đã rà toàn bộ 28 file TXT, gồm ETS2023 làm mẫu. Các khối đáp án dính hai cột ở những năm khác được tách riêng; khôi phục thân câu hỏi xen cột dựa trên toàn bộ câu và lựa chọn đang có trong TXT. Đã xử lý cả các nhãn OCR `(c)` / `(0)` khi thứ tự lựa chọn xác định được rõ.

- Tách từng câu và từng lựa chọn A–D; giữ nội dung lựa chọn, không chọn đáp án thay người học.
- Sắp thứ tự ở 6 phần PART 5 có đủ 30 câu 101–130 và mỗi câu đủ A–D sau khi khôi phục.
- Kiểm tra toàn bộ file: không còn dòng đáp án chứa hai nhãn lựa chọn; không mất nhãn A–D; kiểm tra bảo toàn từ sau khi loại footer và chuẩn hóa nhãn OCR.
- ETS2023 không thay đổi. Những lỗi OCR khác như nhãn thiếu, câu/đáp án nằm xa nhau và phần thân bài bị xáo trộn vẫn cần đối chiếu nguồn; kiểm tra này không xác nhận toàn bộ nội dung OCR đã hoàn chỉnh.
