files = [
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-GuestHomeOverview.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-GuestPersonaVoicePreview.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-GuestGoogleOAuthLogin.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-GuestEmailPasswordSignup.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-GuestEmailConfirmation.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserEmailPasswordLogin.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserMfaEnrollment.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserMfaLoginChallenge.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserMfaResetDevice.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserProfileUpdateDisplayName.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserProfileUploadAvatar.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserForgotPasswordRequest.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserEmailLinkVerificationRedirect.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserResetChangePassword.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserGetSettings.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserUpdateSettings.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserTextChatSse.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserDeleteChat.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserCreateSharedChat.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserRevokeSharedChat.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserBookmarkChat.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-AdminManagePersona.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-AdminSyncElevenLabsVoices.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-AdminCreateVipPlan.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-AdminArchiveVipPlan.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-AdminPhapDienPipelineReport.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-AdminVbplPipelineReport.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-AdminManageVoiceEngine.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserCreateVipPaymentTransaction.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-PaymentGatewayCallbackVerification.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-PaymentSuccessUpdateOutbox.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-PaymentOutboxRelayKafka.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-PaymentSendVipConfirmationEmail.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserTransactionHistoryLookup.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserVoiceLiveKitToken.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserVoiceChatWithAi.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserUploadPersonalDocument.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-DocumentWorkerProcessDocument.tex",
    r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserAnalyzePersonalDocumentRag.tex",
]


def process_latex_file(path):
    try:
        # Đọc nội dung file với bảng mã utf-8
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()

        # Thực hiện thay thế
        # Lưu ý: Dấu \ trong LaTeX cần được escape thành \\ trong chuỗi Python
        # "\n" * 10 tạo ra 10 ký tự xuống dòng
        content = content.replace("\n\\begin", "\n" * 10 + "\n\\begin")
        content = content.replace("\n\\paragraph", "\n" * 10 + "\n\\paragraph")
        content = content.replace("\n\\subparagraph", "\n" * 10 + "\n\\subparagraph")
        content = content.replace("scale = 0.18", "scale = 0.2")
        content = content.replace(
            "Luồng nghiệp vụ này mô tả", "\n" * 10 + "\nLuồng nghiệp vụ này mô tả"
        )
        content = content.replace("\\item", "\n" * 10 + "\n\\item")

        # Ghi lại nội dung đã thay thế vào file
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"Đã xử lý và lưu thành công file:\n{path}")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn {path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


# Chạy hàm xử lý
# process_latex_file(file_path)
for file in files:
    process_latex_file(file)
