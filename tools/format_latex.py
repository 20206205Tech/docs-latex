import os
# import subprocess
from datetime import datetime

# import pyperclip
import settings


def format_latex(directory):
    # print(f"Format markdown gui with root folder = {os.path.abspath(directory)}")
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".tex"):
                file_path = os.path.join(root, file)
                # print(f"Processing file: {file_path}")

                with open(file_path, "r", encoding="utf-8") as f:
                    contents = f.read()








                while "\n\n\n" in contents:
                    contents = contents.replace("\n\n\n", "\n\n")
                contents = contents.replace("\n\n\n", "\n\n")

                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(contents)











                # with open(file_path, "r", encoding="utf-8") as f:
                #     contents = f.readlines()

                # for i in range(len(contents)):

                #     while "{ " in contents[i]:
                #         contents[i] = contents[i].replace("{ ", "{")
                #     contents[i] = contents[i].replace("{ ", "{")

                #     while " }" in contents[i]:
                #         contents[i] = contents[i].replace(" }", "}")
                #     contents[i] = contents[i].replace(" }", "}")

                #     while "( " in contents[i]:
                #         contents[i] = contents[i].replace("( ", "(")
                #     contents[i] = contents[i].replace("( ", "(")

                #     while " )" in contents[i]:
                #         contents[i] = contents[i].replace(" )", ")")
                #     contents[i] = contents[i].replace(" )", ")")

                #     # while " ." in contents[i]:
                #     #     contents[i] = contents[i].replace(" .", ". ")
                #     # contents[i] = contents[i].replace(" .", ". ")

                #     while " ," in contents[i]:
                #         contents[i] = contents[i].replace(" ,", ", ")
                #     contents[i] = contents[i].replace(" ,", ", ")

                #     while " :" in contents[i]:
                #         contents[i] = contents[i].replace(" :", ": ")
                #     contents[i] = contents[i].replace(" :", ": ")

                #     while "  " in contents[i]:
                #         contents[i] = contents[i].replace("  ", " ")
                #     contents[i] = contents[i].replace("  ", " ")

                #     contents[i] = contents[i].strip()

                # contents = "\n".join(contents)
                # with open(file_path, "w", encoding="utf-8") as f:
                #     f.write(contents)






def main(): 
    format_latex(settings.PATH_FOLDER_LATEX)
  


if __name__ == "__main__":
    main()
