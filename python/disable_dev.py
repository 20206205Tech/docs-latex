import os

# Lấy đường dẫn tương đối tới script
script_dir = os.path.dirname(os.path.abspath(__file__))
main_tex_path = os.path.abspath(os.path.join(script_dir, "..", "latex", "main.tex"))

if not os.path.exists(main_tex_path):
    # Thử ở thư mục hiện tại
    main_tex_path = os.path.abspath("latex/main.tex")

if not os.path.exists(main_tex_path):
    raise FileNotFoundError(f"Không tìm thấy main.tex tại {main_tex_path}")

with open(main_tex_path, "r", encoding="utf-8") as f:
    content = f.read()

# Chuẩn hóa dấu xuống dòng thành \n để tránh lỗi giữa Windows (\r\n) và Linux/Mac (\n)
content = content.replace("\r\n", "\n")

# Khai báo chính xác đoạn code cần tìm kiếm
target_block = (
    "\\ifdev\n"
    "\\pagecolor{black} % Thiết lập nền toàn bộ trang PDF thành màu đen\n"
    "\\color{white} % Thiết lập màu chữ mặc định toàn trang là trắng\n"
    "\\fi"
)

# Khai báo đoạn code muốn thay thế vào
replacement_block = "\\devfalse\n" + target_block

# Kiểm tra và tiến hành thay thế
if replacement_block in content:
    print("Dev mode đã được vô hiệu hóa từ trước.")
elif target_block in content:
    new_content = content.replace(target_block, replacement_block)

    # Ghi lại tệp tin
    with open(main_tex_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(new_content)
    print("Đã vô hiệu hóa dev mode thành công cho khối lệnh cấu hình màu.")
else:
    print("Không tìm thấy khối lệnh \\ifdev cấu hình màu trong tệp.")
