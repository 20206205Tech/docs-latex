import glob
import os
import re

PRESERVED_WORDS = {
    "vip": "VIP",
    "livekit": "LiveKit",
    "api": "API",
    "csdl": "CSDL",
    "web frontend": "Web Frontend",
    "api gateway": "API Gateway",
    "kong": "Kong",
    "elevenlabs": "ElevenLabs",
    "milvus": "Milvus",
    "next.js": "Next.js",
    "rabbitmq": "RabbitMQ",
    "r2": "R2",
    "rag": "RAG",
    "mfa": "MFA",
    "2fa": "2FA",
    "sse": "SSE",
    "celery": "Celery",
    "kafka": "Kafka",
    "auth": "Auth",
    "supabase": "Supabase",
    "google": "Google",
    "oauth": "OAuth",
    "ui": "UI",
    "vbpl": "VBPL",
    "ai": "AI",
}


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


def apply_preserved_casing(text, preserved_dict):
    """
    Lowercases text except for words/phrases in the preserved dictionary.
    """
    # Sort keys by length in descending order to match multi-word terms first
    for key in sorted(preserved_dict.keys(), key=len, reverse=True):
        val = preserved_dict[key]
        escaped_key = re.escape(key)
        # Unicode-aware word boundary pattern
        pattern = re.compile(rf"(?<!\w){escaped_key}(?!\w)", re.IGNORECASE)
        text = pattern.sub(val, text)
    return text


def find_env_blocks(content, env_name):
    """
    Finds environment blocks \begin{env_name}[...] ... \end{env_name}
    """
    pattern = re.compile(rf"\\begin\s*\{{{env_name}\}}(?:\[.*?\])?")
    end_str = f"\\end{{{env_name}}}"

    blocks = []
    for match in pattern.finditer(content):
        start_idx = match.start()
        end_idx = content.find(end_str, match.end())
        if end_idx != -1:
            blocks.append((start_idx, end_idx + len(end_str)))
    return blocks


def process_file(filepath):
    """
    Processes a LaTeX file:
    1. Extracts paragraph suffix
    2. Lowercases suffix and applies preserved casing
    3. Aligns and updates paragraph, figure caption, and table caption
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Không thể đọc file {os.path.basename(filepath)}: {e}")
        return False

    cleaned = strip_latex_comments(content)

    # Find paragraph title
    paragraph_titles = []
    pos = 0
    while True:
        pos = cleaned.find("\\paragraph", pos)
        if pos == -1:
            break
        is_sub = pos >= 3 and cleaned[pos - 3 : pos] == "sub"
        if not is_sub:
            val, end_pos = extract_braced_content(cleaned, pos + len("\\paragraph"))
            if val is not None:
                paragraph_titles.append(val.strip())
                pos = end_pos
                continue
        pos += len("\\paragraph")

    paragraph_title = paragraph_titles[0] if paragraph_titles else None

    if not paragraph_title:
        print(f"⚠️  Bỏ qua {os.path.basename(filepath)}: Không tìm thấy \\paragraph")
        return False

    if not paragraph_title.startswith("Sơ đồ tuần tự"):
        print(
            f"⚠️  Bỏ qua {os.path.basename(filepath)}: \\paragraph không bắt đầu bằng 'Sơ đồ tuần tự'"
        )
        return False

    # Extract suffix
    original_suffix = paragraph_title[len("Sơ đồ tuần tự") :].strip()

    # Generate canonical suffix
    suffix_lower = original_suffix.lower()
    clean_suffix = apply_preserved_casing(suffix_lower, PRESERVED_WORDS)

    # Generate edits based on clean_suffix
    edits = []

    # 1. Edit for \paragraph
    pos = 0
    while True:
        pos = content.find("\\paragraph", pos)
        if pos == -1:
            break
        is_sub = pos >= 3 and content[pos - 3 : pos] == "sub"
        if not is_sub:
            brace_start = content.find("{", pos + len("\\paragraph"))
            if brace_start != -1:
                val, end_pos = extract_braced_content(content, pos + len("\\paragraph"))
                if val is not None:
                    new_val = "Sơ đồ tuần tự " + clean_suffix
                    if val.strip() != new_val:
                        edits.append((brace_start + 1, end_pos - 1, new_val))
                    pos = end_pos
                    continue
        pos += len("\\paragraph")

    # 2. Edits for figure captions
    for start_idx, end_idx in find_env_blocks(content, "figure"):
        cap_pos = content.find("\\caption", start_idx, end_idx)
        if cap_pos != -1:
            brace_start = content.find("{", cap_pos + len("\\caption"))
            if brace_start != -1 and brace_start < end_idx:
                val, end_pos = extract_braced_content(
                    content, cap_pos + len("\\caption")
                )
                if val is not None and end_pos <= end_idx:
                    new_val = "Sơ đồ tuần tự " + clean_suffix
                    if val.strip() != new_val:
                        edits.append((brace_start + 1, end_pos - 1, new_val))

    # 3. Edits for table captions
    for start_idx, end_idx in find_env_blocks(content, "table"):
        cap_pos = content.find("\\caption", start_idx, end_idx)
        if cap_pos != -1:
            brace_start = content.find("{", cap_pos + len("\\caption"))
            if brace_start != -1 and brace_start < end_idx:
                val, end_pos = extract_braced_content(
                    content, cap_pos + len("\\caption")
                )
                if val is not None and end_pos <= end_idx:
                    new_val = "Các thành phần tham gia " + clean_suffix
                    if val.strip() != new_val:
                        edits.append((brace_start + 1, end_pos - 1, new_val))

    if not edits:
        return False

    # Apply edits from back to front
    new_content = content
    for start, end, replacement in sorted(edits, key=lambda x: x[0], reverse=True):
        new_content = new_content[:start] + replacement + new_content[end:]

    try:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"✨ Đã cập nhật: {os.path.basename(filepath)}")
        print(f"   -> Suffix mới: '{clean_suffix}'")
        return True
    except Exception as e:
        print(f"❌ Không thể ghi file {os.path.basename(filepath)}: {e}")
        return False


def main():
    directory = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence"
    pattern = os.path.join(directory, "*.tex")
    tex_files = glob.glob(pattern)

    if not tex_files:
        print(f"Không tìm thấy file .tex nào trong thư mục: {directory}")
        return

    print(f"Bắt đầu tự động sửa đổi {len(tex_files)} file .tex...\n")

    updated_count = 0
    for filepath in sorted(tex_files):
        if process_file(filepath):
            updated_count += 1

    print(
        f"\nHoàn thành! Đã sửa đổi thành công {updated_count} / {len(tex_files)} file."
    )


if __name__ == "__main__":
    main()
