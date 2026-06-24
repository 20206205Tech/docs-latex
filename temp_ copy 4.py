import shutil
from pathlib import Path


def clean_unused_images():
    # Định nghĩa các thư mục
    base_dir = Path(r"C:\Users\Admin\Documents\GitHub\docs-latex")
    pictures_dir = base_dir / "latex" / "pictures"
    contents_dir = base_dir / "latex" / "contents"
    temp_dir = pictures_dir / "temp"

    # Định nghĩa các đuôi file
    latex_image_extensions = {".jpeg", ".jpg", ".png"}
    ignore_extensions = {".md", ".mmd", ".puml"}

    print("--- KHỞI TẠO TIẾN TRÌNH KIỂM TRA ẢNH ---")
    print(f"Thư mục ảnh: {pictures_dir}")
    print(f"Thư mục nội dung latex: {contents_dir}")
    print(f"Thư mục chứa ảnh tạm (không dùng): {temp_dir}\n")

    # Tạo thư mục temp nếu chưa tồn tại
    temp_dir.mkdir(parents=True, exist_ok=True)

    # 1. Đọc tất cả nội dung các file .tex trong thư mục contents
    print("Đang đọc nội dung các file .tex...")
    tex_contents = []
    for tex_file in contents_dir.rglob("*.tex"):
        try:
            content = tex_file.read_text(encoding="utf-8")
            tex_contents.append(content)
        except Exception as e:
            print(f" Lỗi khi đọc file {tex_file.name}: {e}")

    print(f" Đã đọc xong {len(tex_contents)} file .tex.\n")

    # 2. Quét các file trong thư mục pictures
    moved_count = 0
    skipped_count = 0
    checked_count = 0

    print("Đang kiểm tra các file ảnh...")
    for item in pictures_dir.iterdir():
        # Bỏ qua nếu là thư mục (ví dụ như thư mục temp hoặc WebUI)
        if not item.is_file():
            continue

        suffix = item.suffix.lower()

        # Kiểm tra nếu thuộc danh sách file bỏ qua
        if suffix in ignore_extensions:
            # print(f" Bỏ qua file theo cấu hình: {item.name}")
            skipped_count += 1
            continue

        # Kiểm tra nếu thuộc danh sách file dùng trong LaTeX
        if suffix in latex_image_extensions:
            checked_count += 1
            name = item.name
            stem = item.stem

            # Kiểm tra xem ảnh có được sử dụng không
            is_used = False
            for content in tex_contents:
                # Kiểm tra các cách tham chiếu ảnh phổ biến trong LaTeX:
                # - Chứa tên file trực tiếp (e.g. Home-vbpl.png)
                # - Chứa đường dẫn có dấu gạch chéo trước tên file (e.g. /Home-vbpl)
                # - Chứa tên trong dấu ngoặc nhọn (e.g. {Home-vbpl})
                if name in content or f"/{stem}" in content or f"{{{stem}}}" in content:
                    is_used = True
                    break

            if not is_used:
                # Di chuyển ảnh không sử dụng vào thư mục temp
                dest_path = temp_dir / name
                print(f"[-] Phát hiện ảnh CHƯA DÙNG: {name} -> Di chuyển vào temp/")
                try:
                    shutil.move(str(item), str(dest_path))
                    moved_count += 1
                except Exception as e:
                    print(f"    Lỗi khi di chuyển file {name}: {e}")
            else:
                # print(f"[+] Ảnh ĐANG DÙNG: {name}")
                pass

    print("\n--- KẾT QUẢ HOÀN THÀNH ---")
    print(f" Tổng số ảnh (.jpg, .jpeg, .png) đã kiểm tra: {checked_count}")
    print(f" Số file bỏ qua (.md, .mmd, .puml): {skipped_count}")
    print(f" Số ảnh chưa dùng đã di chuyển vào temp: {moved_count}")


if __name__ == "__main__":
    clean_unused_images()
