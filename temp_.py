import glob
import os
import re


def extract_braced_content(text, start_pos):
    """
    Finds the content inside the matching braces starting after the first '{'
    found at or after start_pos.
    Returns (content, end_pos) or (None, -1) if not found/unmatched.
    """
    brace_start = text.find("{", start_pos)
    if brace_start == -1:
        return None, -1

    depth = 1
    i = brace_start + 1
    content_chars = []
    while i < len(text):
        char = text[i]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return "".join(content_chars), i + 1
        content_chars.append(char)
        i += 1
    return None, -1


def strip_latex_comments(text):
    """
    Strips LaTeX comments (lines or parts of lines starting with % not preceded by \\).
    """
    lines = []
    for line in text.splitlines():
        cleaned_line = []
        escaped = False
        for char in line:
            if char == "\\":
                escaped = not escaped
            elif char == "%":
                if not escaped:
                    break
                else:
                    escaped = False
            else:
                escaped = False
            cleaned_line.append(char)
        lines.append("".join(cleaned_line))
    return "\n".join(lines)


def check_latex_file(filepath):
    """
    Checks the LaTeX file for the specified conditions:
    1. Paragraph starts with "Sơ đồ tuần tự"
    2. Caption of the figure (image) starts with "Sơ đồ tuần tự"
    3. Caption of the table starts with "Các thành phần tham gia"
    4. All contents following the prefix (i.e. after "Sơ đồ tuần tự" or "Các thành phần tham gia") MUST be lowercase.
    5. The suffix content (after the prefix) must be identical for paragraph, figure, and table.
    """
    violations = []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            raw_content = f.read()
    except Exception as e:
        return [f"Could not read file: {e}"]

    content = strip_latex_comments(raw_content)

    # 1. Find the paragraph
    # Match \paragraph (not \subparagraph)
    paragraph_titles = []
    pos = 0
    while True:
        pos = content.find("\\paragraph", pos)
        if pos == -1:
            break
        # Ensure it's not subparagraph
        is_sub = pos >= 3 and content[pos - 3 : pos] == "sub"
        if not is_sub:
            val, end_pos = extract_braced_content(content, pos + len("\\paragraph"))
            if val is not None:
                paragraph_titles.append(val.strip())
                pos = end_pos
                continue
        pos += len("\\paragraph")

    paragraph_title = paragraph_titles[0] if paragraph_titles else None

    suffix_p = None
    if not paragraph_title:
        violations.append("Không tìm thấy \\paragraph{...}")
    else:
        # Check start of paragraph
        if not paragraph_title.startswith("Sơ đồ tuần tự"):
            violations.append(
                f"\\paragraph không bắt đầu bằng 'Sơ đồ tuần tự': '{paragraph_title}'"
            )
        else:
            suffix_p = paragraph_title[len("Sơ đồ tuần tự") :].strip()
            # Check if all content after "Sơ đồ tuần tự" is lowercase
            if any(c.isupper() for c in suffix_p):
                violations.append(
                    f"Nội dung sau 'Sơ đồ tuần tự' trong paragraph chứa chữ in hoa: '{paragraph_title}'"
                )

    # 2. Find figure blocks and check captions
    figure_blocks = re.findall(
        r"\\begin\s*\{figure\}(?:\[.*?\])?(.*?)\\end\s*\{figure\}", content, re.DOTALL
    )
    figure_captions = []
    for fb in figure_blocks:
        pos = 0
        while True:
            cap_idx = fb.find("\\caption", pos)
            if cap_idx == -1:
                break
            val, end_pos = extract_braced_content(fb, cap_idx + len("\\caption"))
            if val is not None:
                figure_captions.append(val.strip())
                pos = end_pos
            else:
                pos += len("\\caption")

    if not figure_captions:
        violations.append("Không tìm thấy \\caption trong môi trường figure")
    else:
        for cap in figure_captions:
            if not cap.startswith("Sơ đồ tuần tự"):
                violations.append(
                    f"\\caption ảnh không bắt đầu bằng 'Sơ đồ tuần tự': '{cap}'"
                )
            else:
                suffix_f = cap[len("Sơ đồ tuần tự") :].strip()
                # Check lowercase
                if any(c.isupper() for c in suffix_f):
                    violations.append(
                        f"Nội dung sau 'Sơ đồ tuần tự' trong caption ảnh chứa chữ in hoa: '{cap}'"
                    )
                # Check suffix match with paragraph
                if suffix_p is not None and suffix_f != suffix_p:
                    violations.append(
                        f"Nội dung sau 'Sơ đồ tuần tự' của caption ảnh không khớp với paragraph:\n"
                        f"  - paragraph suffix: '{suffix_p}'\n"
                        f"  - caption suffix:   '{suffix_f}'"
                    )

    # 3. Find table blocks and check captions
    table_blocks = re.findall(
        r"\\begin\s*\{table\}(?:\[.*?\])?(.*?)\\end\s*\{table\}", content, re.DOTALL
    )
    table_captions = []
    for tb in table_blocks:
        pos = 0
        while True:
            cap_idx = tb.find("\\caption", pos)
            if cap_idx == -1:
                break
            val, end_pos = extract_braced_content(tb, cap_idx + len("\\caption"))
            if val is not None:
                table_captions.append(val.strip())
                pos = end_pos
            else:
                pos += len("\\caption")

    if not table_captions:
        violations.append("Không tìm thấy \\caption trong môi trường table")
    else:
        for cap in table_captions:
            if not cap.startswith("Các thành phần tham gia"):
                violations.append(
                    f"\\caption bảng không bắt đầu bằng 'Các thành phần tham gia': '{cap}'"
                )
            else:
                suffix_t = cap[len("Các thành phần tham gia") :].strip()
                # Check lowercase
                if any(c.isupper() for c in suffix_t):
                    violations.append(
                        f"Nội dung sau 'Các thành phần tham gia' trong caption bảng chứa chữ in hoa: '{cap}'"
                    )
                # Check suffix match with paragraph
                if suffix_p is not None and suffix_t != suffix_p:
                    violations.append(
                        f"Nội dung sau 'Các thành phần tham gia' của caption bảng không khớp với paragraph:\n"
                        f"  - paragraph suffix: '{suffix_p}'\n"
                        f"  - table suffix:     '{suffix_t}'"
                    )

    return violations


def main():
    directory = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence"
    pattern = os.path.join(directory, "*.tex")
    tex_files = glob.glob(pattern)

    if not tex_files:
        print(f"Không tìm thấy file .tex nào trong thư mục: {directory}")
        return

    print(f"Đang kiểm tra {len(tex_files)} file .tex trong thư mục:\n{directory}\n")

    total_violations = 0
    files_with_violations = 0

    for filepath in sorted(tex_files):
        filename = os.path.basename(filepath)
        violations = check_latex_file(filepath)
        if violations:
            files_with_violations += 1
            total_violations += len(violations)
            print(f"❌ {filename}:")
            for violation in violations:
                print(f"   - {violation}")
            print()

    if total_violations == 0:
        print("✅ Tất cả các file đều đáp ứng các điều kiện!")
    else:
        print(
            f"Tìm thấy {total_violations} lỗi trong {files_with_violations} / {len(tex_files)} files."
        )


if __name__ == "__main__":
    main()
