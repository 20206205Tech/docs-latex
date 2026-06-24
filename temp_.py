import re

# Đường dẫn đến file LaTeX
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Giao_dien_chuong_trinh.tex"


def modify_latex_file(file_path):
    try:
        # 1. Đọc nội dung file gốc
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Tạo bản sao lưu dự phòng (backup) trước khi sửa đổi
        backup_path = file_path + ".bak"
        with open(backup_path, "w", encoding="utf-8") as backup_file:
            backup_file.write(content)
        print(f"Đã tạo file sao lưu tại: {backup_path}")

        # Danh sách lưu các thay đổi để in ra màn hình
        changes = []

        # 2. Hàm callback để xử lý thay thế cho từng caption tìm thấy
        def replace_caption(match):
            original_text = match.group(1)
            # Chuyển thành viết thường
            lowercase_text = original_text.lower()
            # Thêm chữ "Giao diện " ở đầu
            new_text = f"Giao diện {lowercase_text}"

            changes.append((original_text, new_text))
            return f"\\caption{{{new_text}}}"

        # Thay thế \caption{...} bằng \caption{Giao diện <viết thường>}
        updated_content = re.sub(r"\\caption\{([^}]+)\}", replace_caption, content)

        # 3. Ghi đè nội dung đã sửa đổi vào file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(updated_content)

        print(f"Đã cập nhật file thành công! Chi tiết các thay đổi:")
        print("-" * 75)
        for i, (orig, new) in enumerate(changes, 1):
            print(f"{i:02d} | Cũ: \\caption{{{orig}}}")
            print(f"   | Mới: \\caption{{{new}}}")
            print("-" * 75)

    except FileNotFoundError:
        print(f"Không tìm thấy file: {file_path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


if __name__ == "__main__":
    modify_latex_file(file_path)
