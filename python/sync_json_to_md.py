# import os

# DATA = [


# ]


# def generate_markdown():
#     # Path relative to the root of the repository
#     md_path = os.path.join("docs", "0", "9.md")

#     # Sắp xếp theo Từ viết tắt (A-Z)
#     sorted_data = sorted(DATA, key=lambda x: x["abbr"])

#     # Tạo nội dung Markdown
#     md_content = "# Danh sách viết tắt\n\n"
#     md_content += "| Từ viết tắt | Từ viết đầy đủ | Mô tả |\n"
#     md_content += "| --- | --- | --- |\n"

#     for item in sorted_data:
#         md_content += f"| {item['abbr']} | {item['eng']} | {item['vie']} |\n"

#     # Ghi ra file markdown
#     with open(md_path, "w", encoding="utf-8") as f:
#         f.write(md_content)

#     print(f"Successfully updated {md_path}")


# if __name__ == "__main__":
#     generate_markdown()
