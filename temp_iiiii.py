import re
from pathlib import Path

from loguru import logger

target_path = Path(r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\service")
target_path = Path(r"C:\Users\Admin\Documents\GitHub\docs-latex\latex")

if not target_path.exists():
    logger.error(f"Đường dẫn không tồn tại: {target_path}")
else:
    files_to_process = []
    base_path = target_path

    # KIỂM TRA ĐIỀU KIỆN: Nếu là file đơn lẻ
    if target_path.is_file():
        if target_path.suffix == ".tex":
            files_to_process = [target_path]
            base_path = (
                target_path.parent
            )  # Lấy thư mục cha để hiển thị log relative gọn hơn
            logger.info(f"Phát hiện tệp đơn lẻ, bắt đầu xử lý: {target_path.name}")
        else:
            logger.error("Tệp được chọn không phải là định dạng .tex")

    # KIỂM TRA ĐIỀU KIỆN: Nếu là thư mục
    elif target_path.is_dir():
        files_to_process = list(target_path.rglob("*.tex"))
        logger.info(
            f"Phát hiện thư mục, bắt đầu quét toàn bộ file .tex trong: {target_path}"
        )

    # Biến đếm thống kê
    total_files = 0
    total_replaced = 0

    # Cấu hình Regex tìm kiếm và chuỗi thay thế
    search_pattern = re.compile(r"\\includegraphics\[.*?\]")
    replace_str = r"\\includegraphics[width=0.75\\textwidth]"

    # Vòng lặp xử lý danh sách file đã lọc được ở trên
    for file_path in files_to_process:
        total_files += 1

        relative_path = file_path.relative_to(base_path)
        logger.info(f"Đang xử lý file: {relative_path}")

        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        new_lines = []
        modified = False

        for index, line in enumerate(lines):
            if search_pattern.search(line):
                new_line, num_subs = search_pattern.subn(replace_str, line)
                new_lines.append(new_line)

                total_replaced += num_subs
                modified = True

                logger.warning(
                    f"  -> Dòng {index + 1}: Đã thay thế {num_subs} vị trí | Nội dung mới: {new_line.strip()}"
                )
            else:
                new_lines.append(line)

        if modified:
            with open(file_path, "w", encoding="utf-8") as file:
                file.writelines(new_lines)
            logger.success(f"Đã cập nhật file: {relative_path}")
        else:
            logger.info(f"Không có thay đổi nào trong file: {relative_path}")

    logger.info("=" * 50)
    logger.success(f"Quá trình hoàn tất!")
    logger.info(f"Tổng số file đã quét: {total_files}")
    logger.info(f"Tổng số chuỗi đã thay thế: {total_replaced}")
