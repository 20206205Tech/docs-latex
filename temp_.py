from pathlib import Path


def find_tex_files_and_export():
    # Đường dẫn thư mục cần quét
    folder_path = Path(r"C:\Users\Admin\Documents\GitHub\docs-latex\latex")

    # Tên file đầu ra
    output_filename = "output.md"

    # Kiểm tra xem thư mục có tồn tại không
    if not folder_path.exists() or not folder_path.is_dir():
        print(f"Lỗi: Thư mục '{folder_path}' không tồn tại hoặc không hợp lệ.")
        return

    # Mở file output.md để ghi với encoding utf-8 để hỗ trợ tiếng Việt
    with open(output_filename, "w", encoding="utf-8") as output_file:
        # Hàm rglob("*.tex") sẽ tìm tất cả các file .tex trong folder và folder con
        for file_path in folder_path.rglob("*.tex"):
            # Lấy đường dẫn tuyệt đối đầy đủ của file
            full_path = file_path.resolve()

            # Ghi vào file markdown theo định dạng yêu cầu
            output_file.write(f"Đường dẫn: {full_path}\n")

    print(f"Đã quét xong! Kết quả được lưu tại file: {output_filename}")


if __name__ == "__main__":
    find_tex_files_and_export()
