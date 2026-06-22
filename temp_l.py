from pathlib import Path

from loguru import logger

directory_path = Path(r"C:\Users\Admin\Documents\GitHub\docs-latex\latex")

if not directory_path.exists():
    logger.error(f"Thư mục không tồn tại: {directory_path}")
else:
    logger.info(f"Bắt đầu quét thư mục gốc VÀ các thư mục con: {directory_path}")

    # Biến đếm thống kê
    total_files = 0
    total_deleted = 0

    # Dùng rglob() thay cho glob() để đệ quy vào tất cả các thư mục con
    for file_path in directory_path.rglob("*.tex"):
        total_files += 1

        # Lấy đường dẫn tương đối so với thư mục gốc để hiển thị log dễ nhìn hơn
        relative_path = file_path.relative_to(directory_path)
        logger.info(f"Đang xử lý file: {relative_path}")

        with open(file_path, "r", encoding="utf-8") as file:
            lines = file.readlines()

        new_lines = []
        modified = False

        for index, line in enumerate(lines):
            # Nếu phát hiện \label, bỏ qua không thêm vào new_lines (tức là xóa)
            if r"\label" in line:
                logger.warning(f"  -> Dòng {index + 1}: XÓA | Nội dung: {line.strip()}")
                total_deleted += 1
                modified = True
                continue
            else:
                new_lines.append(line)

        # Chỉ ghi đè lại file nếu có sự thay đổi
        if modified:
            with open(file_path, "w", encoding="utf-8") as file:
                file.writelines(new_lines)
            logger.success(f"Đã cập nhật file: {relative_path}")
        else:
            logger.info(f"Không có thay đổi nào trong file: {relative_path}")

    logger.info("=" * 50)
    logger.success(f"Quá trình hoàn tất!")
    logger.info(f"Tổng số file đã quét: {total_files}")
    logger.info(f"Tổng số dòng đã xóa: {total_deleted}")
