# from pathlib import Path


# def get_file_types(directory_path):
#     path = Path(directory_path)

#     # Kiểm tra xem đường dẫn có tồn tại và là thư mục không
#     if not path.exists():
#         print(f"Đường dẫn không tồn tại: {directory_path}")
#         return set()
#     if not path.is_dir():
#         print(f"Đường dẫn không phải là thư mục: {directory_path}")
#         return set()

#     # Tập hợp (set) để lưu các loại file duy nhất
#     file_types = set()

#     # Duyệt qua các tệp tin trong thư mục
#     for item in path.iterdir():
#         if item.is_file():
#             # Lấy đuôi file (ví dụ: '.png', '.jpg', '.webp') và chuyển về dạng viết thường
#             suffix = item.suffix.lower()
#             if suffix:
#                 file_types.add(suffix)
#             else:
#                 file_types.add("(không có đuôi file)")

#     return file_types


# if __name__ == "__main__":
#     target_dir = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\pictures"

#     types = get_file_types(target_dir)

#     print(f"Các loại file tìm thấy trong thư mục '{target_dir}':")
#     for file_type in sorted(types):
#         print(f" - {file_type}")

# Định nghĩa các file:

# file dùng trong latex:
# - .jpeg
# - .jpg
# - .png

# file bỏ qua:
# - .md
# - .mmd
# - .puml

# Kiểm tra trong
# C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents
# nếu ảnh nào không dùng sẽ di chuyển vào
# C:\Users\Admin\Documents\GitHub\docs-latex\latex\pictures\temp
