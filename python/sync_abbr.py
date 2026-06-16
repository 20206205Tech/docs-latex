import os
import sys

import env

if sys.stdout.encoding != "utf-8":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        import codecs

        sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer)


DATA = [
    {"abbr": "GPU", "eng": "Graphics Processing Unit", "vie": "Bộ phận xử lý đồ họa"},
    {"abbr": "AI", "eng": "Artificial Intelligence", "vie": "Trí tuệ nhân tạo"},
    {
        "abbr": "NLP",
        "eng": "Natural Language Processing",
        "vie": "Xử lý ngôn ngữ tự nhiên",
    },
    {"abbr": "LLM", "eng": "Large Language Model", "vie": "Mô hình ngôn ngữ lớn"},
    {
        "abbr": "API",
        "eng": "Application Programming Interface",
        "vie": "Giao diện lập trình ứng dụng",
    },
    {
        "abbr": "RAG",
        "eng": "Retrieval Augmented Generation",
        "vie": "Tạo tăng cường truy xuất",
    },
    {"abbr": "DDD", "eng": "Domain Driven Design", "vie": "Thiết kế hướng miền"},
    {"abbr": "MSA", "eng": "Microservice Architecture", "vie": "Kiến trúc vi dịch vụ"},
    {
        "abbr": "SQL",
        "eng": "Structured Query Language",
        "vie": "Ngôn ngữ truy vấn cấu trúc",
    },
    {
        "abbr": "JWT",
        "eng": "JSON Web Token",
        "vie": "Tiêu chuẩn truyền tải thông tin JSON",
    },
    {
        "abbr": "JSON",
        "eng": "JavaScript Object Notation",
        "vie": "Một kiểu định dạng dữ liệu key - value",
    },
    {
        "abbr": "RLS",
        "eng": "Row-Level Security",
        "vie": "Bảo mật cấp hàng",
    },
    # {
    #     "abbr": "OOP",
    #     "eng": "Object-Oriented Programming",
    #     "vie": "Lập trình hướng đối tượng",
    # },
    {
        "abbr": "URL",
        "eng": "Uniform Resource Locator",
        "vie": "Định danh tài nguyên Internet",
    },
    {"abbr": "CLI", "eng": "Command Line Interface", "vie": "Giao diện dòng lệnh"},
    {"abbr": "CSDL", "eng": "Cơ sở dữ liệu", "vie": "Cơ sở dữ liệu"},
    {"abbr": "SSE", "eng": "Server-sent events", "vie": "Sự kiện máy chủ gửi"},
    {
        "abbr": "TOTP",
        "eng": "Time-based One-Time Password",
        "vie": "Mật khẩu dùng một lần dựa trên thời gian",
    },
    {"abbr": "2FA", "eng": "Two-Factor Authentication", "vie": "Xác thực hai yếu tố"},
    {"abbr": "MFA", "eng": "Multi-Factor Authentication", "vie": "Xác thực đa yếu tố"},
    {"abbr": "VIP", "eng": "Very Important Person", "vie": "Người rất quan trọng"},
    {"abbr": "K8s", "eng": "Kubernetes", "vie": "Kubernetes"},
    {"abbr": "CI", "eng": "Continuous Integration", "vie": "Tích hợp liên tục"},
    {
        "abbr": "CD",
        "eng": "Continuous Delivery / Deployment",
        "vie": "Chuyển giao/Triển khai liên tục",
    },
    {
        "abbr": "HTML",
        "eng": "Hyper Text Markup Language",
        "vie": "Ngôn ngữ Đánh dấu Siêu văn bản",
    },
    {
        "abbr": "TTS",
        "eng": "Text to Speech",
        "vie": "Chuyển văn bản thành giọng nói",
    },
    {
        "abbr": "STT",
        "eng": "Speech to Text",
        "vie": "Chuyển giọng nói thành văn bản",
    },
    {
        "abbr": "IaC",
        "eng": "Infrastructure as Code",
        "vie": "Cơ sở hạ tầng dưới dạng mã",
    },
    {
        "abbr": "SMTP",
        "eng": "Simple Mail Transfer Protocol",
        "vie": "Giao thức truyền thư đơn giản",
    },
    {
        "abbr": "IPN",
        "eng": "Instant Payment Notification",
        "vie": "Thông báo thanh toán tức thì",
    },
    {
        "abbr": "PSP",
        "eng": "Payment Service Provider",
        "vie": "Đơn vị cung cấp dịch vụ thanh toán",
    },
    {
        "abbr": "PSC",
        "eng": "Payment Service Consumer",
        "vie": "Đơn vị sử dụng dịch vụ thanh toán",
    },
    {
        "abbr": "UI",
        "eng": "User Interface",
        "vie": "Giao diện người dùng",
    },
    {
        "abbr": "gRPC",
        "eng": "gRPC Remote Procedure Call",
        "vie": "Framework Gọi thủ tục từ xa do Google phát triển",
    },
    {
        "abbr": "DLQ",
        "eng": "Dead Letter Queue",
        "vie": "Hàng đợi thư lỗi",
    },
    {
        "abbr": "QR Code",
        "eng": "Quick Response Code",
        "vie": "Mã phản hồi nhanh",
    },
]


# OCR	Optical Character Recognition (Công nghệ nhận dạng chữ qua ảnh)

# # Ack
# # <!-- UML -->


# # CQRS (Command Query Responsibility Segregation)

# # là mẫu thiết kế tách biệt mô hình dữ liệu cho các thao tác đọc (Query) và ghi (Command). Việc tách biệt này giúp tối ưu hóa hiệu suất, tăng khả năng mở rộng (scalability), bảo mật tốt hơn và quản lý độ phức tạp trong các hệ thống lớn

# # <!-- CQRS là viết tắt của Command and Query Responsibility Segregation -->


# \textbf{STT} & \textbf{Từ viết tắt} & \textbf{Từ viết đầy đủ} & \textbf{Mô tả} \\ \hline

# 1 & CNTT & Công nghệ thông tin & Công nghệ thông tin \\ \hline

# 2 & OOP & Object Oriented Programming & \makecell[l]{Kỹ thuật lập trình \\ hướng đối tượng} \\ \hline
# 3 & ORM & Object Relational Mapping & \makecell[l]{Kỹ thuật ánh xạ \\ các đối tượng lập trình\\ với từng bảng trong\\ cơ sở dữ liệu} \\ \hline


# 5 & DBMS & Database Management System & \makecell[l]{Hệ quản trị cơ sở dữ liệu} \\ \hline


# 9 & HMAC & Hash-based Message Authentication Code & \makecell[l]{Mã xác thực tin nhắn \\ dựa trên băm} \\ \hline


# 12 & QR Code & Quick response code & Mã phản hồi nhanh \\ \hline
# 16 & TTL & Time To Live & \makecell[l]{Thời gian bản ghi DNS \\ được lưu trữ trong\\ bộ nhớ cache} \\ \hline

# 14 & DNS & Domain Name System & \makecell[l]{Hệ thống phân giải \\ tên miền} \\ \hline
# 15 & FQDN & Fully Qualified Domain Name & Tên miền đầy đủ \\ \hline
# 20 & XDR & Extended Detection and Response & \makecell[l]{Phát hiện và \\ ứng phó mở rộng} \\ \hline
# 17 & BIND9 & Berkeley Internet Name Domain & \makecell[l]{Một phần mềm \\ máy chủ DNS} \\ \hline


TEX_PATH = os.path.join(
    env.PATH_FOLDER_LATEX,
    "contents",
    "0",
    "danh_sach_viet_tat",
    "danh_sach_viet_tat.tex",
)

# Số ký tự tối đa trong một dòng của cột Mô tả trước khi xuống dòng (\\)
MAX_LINE_LENGTH = 40


def wrap_text(text: str, max_length: int = MAX_LINE_LENGTH) -> str:
    """Tự động ngắt dòng dài thành makecell nếu vượt quá max_length ký tự."""
    if len(text) <= max_length:
        return text

    words = text.split()
    lines = []
    current = ""

    for word in words:
        if current and len(current) + 1 + len(word) > max_length:
            lines.append(current)
            current = word
        else:
            current = (current + " " + word).strip()

    if current:
        lines.append(current)

    if len(lines) == 1:
        return lines[0]

    return r"\makecell[l]{" + r" \\ ".join(lines) + "}"


def check_duplicates():
    seen = {}
    duplicates = []
    for item in DATA:
        abbr = item["abbr"]
        if abbr in seen:
            duplicates.append(abbr)
        else:
            seen[abbr] = True
    if duplicates:
        raise ValueError(f"Duplicate abbreviations found: {', '.join(duplicates)}")


def generate_tex():
    check_duplicates()
    sorted_data = sorted(DATA, key=lambda x: x["abbr"])

    rows = []
    for i, item in enumerate(sorted_data, start=1):
        vie_cell = wrap_text(item["vie"])
        row = f"{i} & {item['abbr']} & {item['eng']} & {vie_cell} \\\\ \\hline"
        rows.append(row)

    rows_str = "\n".join(rows)

    tex_content = rf"""\newpage
{{\centering \section*{{DANH MỤC KÝ HIỆU}}}} % Đặt tên tiêu đề
\addcontentsline{{toc}}{{section}}{{DANH MỤC KÝ HIỆU}} % Thêm vào mục lục

\begin{{table}}[ht]
\centering
\begin{{tabular}}{{|c|c|c|l|}}
\hline
\textbf{{STT}} & \textbf{{Từ viết tắt}} & \textbf{{Từ viết đầy đủ}} & \textbf{{Mô tả}} \\ \hline
{rows_str}
\end{{tabular}}
\end{{table}}

\newpage
"""

    os.makedirs(os.path.dirname(TEX_PATH), exist_ok=True)

    with open(TEX_PATH, "w", encoding="utf-8") as f:
        f.write(tex_content)

    print(f"Successfully updated: {TEX_PATH}")


if __name__ == "__main__":
    generate_tex()
