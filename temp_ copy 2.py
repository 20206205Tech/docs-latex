import os
import re
from collections import defaultdict
from pathlib import Path


def find_matching_brace(text, start_idx):
    """
    Tìm vị trí của dấu đóng ngoặc nhọn '}' tương ứng với dấu mở ngoặc nhọn '{' tại start_idx.
    Hỗ trợ xử lý các dấu ngoặc nhọn lồng nhau.
    """
    brace_count = 0
    for idx in range(start_idx, len(text)):
        char = text[idx]
        # Bỏ qua các dấu ngoặc nhọn đã được escape bằng dấu gạch chéo ngược (ví dụ: \{ hoặc \})
        if char == "{" and (idx == 0 or text[idx - 1] != "\\"):
            brace_count += 1
        elif char == "}" and (idx == 0 or text[idx - 1] != "\\"):
            brace_count -= 1
            if brace_count == 0:
                return idx
    return -1


def clean_latex_comments(text):
    """
    Loại bỏ các đoạn chú thích (comment) trong LaTeX (bắt đầu bằng dấu '%' không được escape).
    Thay thế các ký tự chú thích bằng khoảng trắng để giữ nguyên chỉ số (index) và số dòng của file gốc.
    """
    chars = list(text)
    is_escaped = False
    in_comment = False

    for i, char in enumerate(chars):
        if in_comment:
            if char == "\n":
                in_comment = False
            else:
                chars[i] = " "  # Thay thế bằng khoảng trắng để giữ nguyên index dòng
        else:
            if char == "\\":
                is_escaped = not is_escaped
            elif char == "%":
                if not is_escaped:
                    in_comment = True
                    chars[i] = " "
                is_escaped = False
            else:
                is_escaped = False

    return "".join(chars)


def extract_captions(file_path):
    """
    Trích xuất toàn bộ caption và số dòng tương ứng từ file LaTeX.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"Lỗi khi đọc file {file_path}: {e}")
        return []

    cleaned_content = clean_latex_comments(content)
    captions = []

    # Tìm tag \caption, hỗ trợ cả tham số tùy chọn \caption[short]{long} hoặc khoảng trắng tùy ý
    pattern = r"\\caption\s*(?:\[[^\]]*\])?\s*\{"

    for match in re.finditer(pattern, cleaned_content):
        start_bracket_idx = match.end() - 1  # Vị trí dấu '{'
        end_bracket_idx = find_matching_brace(cleaned_content, start_bracket_idx)

        if end_bracket_idx != -1:
            caption_raw = cleaned_content[start_bracket_idx + 1 : end_bracket_idx]
            # Chuẩn hóa khoảng trắng và dấu xuống dòng trong caption
            caption_clean = " ".join(caption_raw.split())

            # Tính toán số dòng (1-based index)
            line_num = content.count("\n", 0, match.start()) + 1
            captions.append((caption_clean, line_num))

    return captions


def main():
    target_dir = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex"
    print(f"Đang quét thư mục: {target_dir}\n")

    caption_locations = defaultdict(list)
    total_files = 0
    total_captions_count = 0

    path = Path(target_dir)
    if not path.exists():
        print(f"Lỗi: Thư mục '{target_dir}' không tồn tại.")
        return

    # Quét đệ quy qua toàn bộ thư mục và các thư mục con
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(".tex"):
                file_path = Path(root) / file
                total_files += 1

                # Lấy đường dẫn tương đối để hiển thị đẹp hơn
                try:
                    rel_path = file_path.relative_to(path)
                except ValueError:
                    rel_path = file_path

                captions = extract_captions(file_path)
                for caption, line_num in captions:
                    caption_locations[caption].append((rel_path, line_num))
                    total_captions_count += 1

    print(f"Đã quét: {total_files} file .tex")
    print(f"Tổng số caption tìm thấy: {total_captions_count}")
    print(f"Số lượng caption duy nhất (không trùng lặp): {len(caption_locations)}\n")

    # Tìm và lọc ra các caption bị trùng lặp
    duplicates = {cap: locs for cap, locs in caption_locations.items() if len(locs) > 1}

    if duplicates:
        print(f"CẢNH BÁO: Phát hiện {len(duplicates)} caption bị trùng lặp:\n")
        for idx, (caption, locs) in enumerate(duplicates.items(), 1):
            print(f'{idx}. Nội dung Caption: "{caption}"')
            print(f"   Xuất hiện {len(locs)} lần tại:")
            for file, line in locs:
                print(f"     - File: {file} (Dòng {line})")
            print()
    else:
        print("Chúc mừng: Không phát hiện caption nào bị trùng lặp!")


if __name__ == "__main__":
    main()
