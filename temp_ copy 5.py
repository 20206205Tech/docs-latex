import re

# Đường dẫn đến file LaTeX
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Giao_dien_chuong_trinh.tex"


def extract_captions(file_path):
    try:
        # Đọc nội dung file với mã hóa utf-8
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Sử dụng biểu thức chính quy (Regular Expression) để tìm tất cả các cụm \caption{...}
        # ([^}]+) sẽ khớp với toàn bộ ký tự bên trong dấu ngoặc nhọn {} không chứa dấu đóng ngoặc }
        captions = re.findall(r"\\caption\{([^}]+)\}", content)

        return captions
    except FileNotFoundError:
        print(f"Không tìm thấy file tại đường dẫn: {file_path}")
        return []
    except Exception as e:
        print(f"Đã xảy ra lỗi khi đọc file: {e}")
        return []


if __name__ == "__main__":
    captions = extract_captions(file_path)

    print(f"Tìm thấy tất cả {len(captions)} caption trong file:")
    print("-" * 50)
    for index, caption in enumerate(captions, 1):
        print(f"Caption {index}: {caption}")
