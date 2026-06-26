import os
import shutil

# Đường dẫn thư mục nguồn (chứa file hiện tại)
source_folder = r"C:\Users\Admin\Documents\git\service\images"

# Đường dẫn thư mục đích (nơi muốn chuyển file tới)
dest_folder = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\pictures"

# Danh sách các file cần chuyển
files_to_move = [
    "conversation-and-chatbot-overview.png",
    "conversation-swagger.png",
    "delete-chat-validation-share.png",
    "conversation-PR.png",
    "conversation-lint.png",
    "conversation-database-migration.png",
    "conversation-database.png",
    "chatbot-swagger.png",
    "chatbot-database-migration.png",
    "chatbot-database.png",
    "share-out-of-order.png",
    "share-out-of-order.mmd",
    "dlq-telegram-alert.png",
    "dlq-telegram-alert.mmd",
    "share-concurrency-handling.png",
    "share-concurrency-handling.mmd",
    "voice-livekit-overview.png",
    "voice-clean_transcript.png",
    "r2chat.png",
    "voice-developer-send-text.png",
    "voice-get-persona-ui.png",
    "voice-get-persona-terminal.png",
]


def move_files(src, dest, files):
    # 1. Kiểm tra thư mục nguồn
    if not os.path.exists(src):
        print(f"❌ Lỗi: Không tìm thấy thư mục nguồn '{src}'.")
        return

    # 2. Tạo thư mục đích nếu chưa tồn tại
    if not os.path.exists(dest):
        try:
            os.makedirs(dest)
            print(f"📁 Đã tạo thư mục đích: '{dest}'")
        except Exception as e:
            print(f"❌ Lỗi không thể tạo thư mục đích: {e}")
            return

    print(f"--- BẮT ĐẦU CHUYỂN FILE ---\n")

    # 3. Tiến hành chuyển từng file
    for filename in files:
        src_path = os.path.join(src, filename)
        dest_path = os.path.join(dest, filename)

        if os.path.isfile(src_path):
            try:
                # Dùng shutil.move để Cắt (Cut)         và          Dán (Paste)
                shutil.move(src_path, dest_path)
                print(f"✅ Đã chuyển thành công: {filename}")
            except Exception as e:
                print(f"⚠️ Lỗi khi chuyển '{filename}': {e}")
        else:
            print(f"❌ Bỏ qua (Không tìm thấy ở thư mục nguồn): {filename}")

    print("\n🎉 Hoàn tất quá trình chuyển file!")


if __name__ == "__main__":
    move_files(source_folder, dest_folder, files_to_move)
