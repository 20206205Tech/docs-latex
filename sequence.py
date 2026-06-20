# Đường dẫn tới file LaTeX
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-GuestHomeOverview.tex"


def process_latex_file(path):
    try:
        # Đọc nội dung file với bảng mã utf-8
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()

        # Thực hiện thay thế
        # Lưu ý: Dấu \ trong LaTeX cần được escape thành \\ trong chuỗi Python
        # "\n" * 10 tạo ra 10 ký tự xuống dòng
        content = content.replace("\n\\begin", "\n" * 10 + "\n\\begin")
        content = content.replace("\n\\paragraph", "\n" * 10 + "\n\\paragraph")
        content = content.replace("\n\\subparagraph", "\n" * 10 + "\n\\subparagraph")

        # Ghi lại nội dung đã thay thế vào file
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"Đã xử lý và lưu thành công file:\n{path}")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn {path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


# Chạy hàm xử lý
process_latex_file(file_path)
