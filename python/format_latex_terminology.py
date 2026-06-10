import sys

import env

# Ensure console output handles UTF-8 for Vietnamese characters
if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        import codecs

        sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer)


def format_terminology(content):
    # Skip LaTeX comments (% ...) to avoid modifying them
    # Split on comment lines to preserve them
    lines = content.split("\n")
    result = []

    for line in lines:
        # Find where the comment starts (% not preceded by \)
        comment_idx = -1
        for i, ch in enumerate(line):
            if ch == "%" and (i == 0 or line[i - 1] != "\\"):
                comment_idx = i
                break

        if comment_idx == -1:
            # No comment — process entire line
            text_part = line
            comment_part = ""
        else:
            text_part = line[:comment_idx]
            comment_part = line[comment_idx:]

        # Terminology replacement (add your terms below)
        text_part = text_part.replace("hội thoại", "trò chuyện")
        text_part = text_part.replace("HỘI THOẠI", "TRÒ CHUYỆN")

        result.append(text_part + comment_part)

    return "\n".join(result)


def process_latex():
    latex_dir = env.PATH_FOLDER_LATEX

    if not latex_dir or not __import__("os").path.exists(latex_dir):
        print(f"Directory not found: {latex_dir}")
        return

    from pathlib import Path

    for tex_file in Path(latex_dir).rglob("*.tex"):
        try:
            with open(tex_file, "r", encoding="utf-8") as f:
                content = f.read()

            formatted_content = format_terminology(content)

            if content != formatted_content:
                with open(tex_file, "w", encoding="utf-8") as f:
                    f.write(formatted_content)
                print(f"Updated: {tex_file}")
        except Exception as e:
            print(f"Error processing {tex_file}: {e}")


if __name__ == "__main__":
    process_latex()
