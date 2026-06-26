import os
import re

# Get path relative to this script
script_dir = os.path.dirname(os.path.abspath(__file__))
main_tex_path = os.path.abspath(os.path.join(script_dir, "..", "latex", "main.tex"))

if not os.path.exists(main_tex_path):
    # Try current working directory
    main_tex_path = os.path.abspath("latex/main.tex")

if not os.path.exists(main_tex_path):
    raise FileNotFoundError(f"main.tex not found at {main_tex_path}")

with open(main_tex_path, "r", encoding="utf-8") as f:
    content = f.read()

# Check if it was already replaced
if "\\devfalse\n\\ifdev" not in content and "\\devfalse\r\n\\ifdev" not in content:
    # Replace \ifdev on a line by itself using lambda to prevent regex escape issues
    new_content, count = re.subn(
        r"(?m)^\\ifdev\s*$", lambda m: "\\devfalse\n\\ifdev", content
    )
    if count > 0:
        with open(main_tex_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        print("Disabled dev mode in main.tex successfully using regex.")
    else:
        print("Could not find stand-alone \\ifdev line.")
else:
    print("Dev mode is already disabled.")
