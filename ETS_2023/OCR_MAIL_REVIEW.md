# Các thông tin mail cần đối chiếu bản gốc

Đã rà và sửa phần đầu mail trong TEST2–TEST10 theo cách trình bày của TEST1: tách từng mail, gắn giá trị vào To/From/Cc/Date/Subject/Attachment và tách khỏi nội dung. TEST1 do người dùng sửa được giữ nguyên. Không thay đổi PART1–PART6.

Các giá trị khôi phục dựa trên TXT và bản lưu trước khi dọn OCR. Ví dụ: TEST2, câu 186–190, mail gửi Carlos Cruz có ngày `November 11`; lần dọn trước đã xóa nhầm `11`, nay đã phục hồi.

## Các trường chưa đủ dữ liệu

| Test / bài | Trường | Dữ liệu hiện có / việc cần kiểm tra |
| --- | --- | --- |
| TEST4 / 186–190, mail thứ hai | From | OCR là `qrines@islandlink.bt»`; chưa xác định chắc phần cuối địa chỉ. Giữ nguyên chuỗi OCR. |
| TEST5 / 153–154 | Date | OCR là `January To ^`; chưa đọc chắc số ngày. Giữ nguyên để đối chiếu. |
| TEST7 / 186–190 | Địa chỉ mail | Có các biến thể OCR `foursquarehousing.conr` / `foursquarehousing.com`, `waidertechnology.com` / `wardertechnology.com`. Đã gắn đúng nhãn, chưa tự đồng nhất địa chỉ. |
| TEST7 / 191–195, mail thứ hai | Date | OCR là `February-!^`; chưa đọc chắc số ngày. Giữ nguyên để đối chiếu. |
| TEST10 / 191–195 | Subject / Attachment | Hai giá trị `Notes` và `Information on rough cut of video` bị dính vào cùng một dòng OCR. Đã tách thành `Subject: Notes`, `Attachment: Information on rough cut of video`; cần đối chiếu ảnh gốc để xác nhận cách gắn hai giá trị. |

Các tên, địa chỉ hoặc miền mail có lỗi nhận dạng chưa chắc chắn khác được giữ theo TXT; không tự tạo địa chỉ thay thế.

## TEST6: phần đầu mail không có trong bản TXT trước khi dọn

Chỉ tái dựng To/From từ lời chào, chữ ký và nội dung. Đây là thông tin suy ra từ bài, chưa phải bản chép lại đầy đủ header gốc. Không bổ sung Date/Subject khi không có căn cứ.

| Bài | To / From đã tái dựng | Còn thiếu |
| --- | --- | --- |
| 159–161 | To: Mr. Foster; From: Ken Iwata, Customer Support, Natural Spring Garden Products | Ngày gửi, chủ đề, địa chỉ mail gốc |
| 176–180, mail hỏi | To: Bridget Morandi; From: Marybeth Wright | Ngày gửi, chủ đề, địa chỉ mail gốc |
| 176–180, mail trả lời | To: Marybeth Wright; From: Bridget Morandi | Ngày gửi, chủ đề, địa chỉ mail gốc |
| 191–195 | To: Kevin Oessenich; From: Skye Botha, Western Cape Eats | Ngày gửi, chủ đề, địa chỉ mail gốc |

Bài 176–180 đã đưa mail hỏi của Marybeth trước mail trả lời của Bridget. Lời hồi đáp và câu 178 hỏi từ `drop` trong “the first e-mail” hỗ trợ thứ tự này. Nội dung hai mail giữ nguyên.

Bài 181–185 thiếu tiêu đề nhóm trong TXT. Đã bổ sung `Questions 181-185 refer to the following article and letter.` trước bài báo và thư tương ứng; đây là tiêu đề dựng lại từ loại văn bản và số câu hiện có.

## Kiểm tra

- Tất cả câu hỏi và số lượng lựa chọn A–D trong TEST2–TEST10 được giữ lại.
- PART1–PART6 của TEST2–TEST10 không thay đổi trong lần sửa mail này.
- TEST1 không thay đổi trong lần sửa này.
- Không còn các trường To/From/Date/Subject/Cc/Attachment trống, rời khỏi giá trị sẵn có.
