file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-GuestHomeOverview.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-GuestPersonaVoicePreview.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-GuestGoogleOAuthLogin.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-GuestEmailPasswordSignup.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-GuestEmailConfirmation.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserEmailPasswordLogin.tex"


file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserMfaEnrollment.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserMfaLoginChallenge.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserMfaResetDevice.tex"


file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserProfileUpdateDisplayName.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserProfileUploadAvatar.tex"


file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserForgotPasswordRequest.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserEmailLinkVerificationRedirect.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserResetChangePassword.tex"


file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserGetSettings.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserUpdateSettings.tex"


file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserTextChatSse.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserDeleteChat.tex"


file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserCreateSharedChat.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserRevokeSharedChat.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserBookmarkChat.tex"


file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-AdminManagePersona.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-AdminSyncElevenLabsVoices.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-AdminCreateVipPlan.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-AdminArchiveVipPlan.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-AdminPhapDienPipelineReport.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-AdminVbplPipelineReport.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-AdminManageVoiceEngine.tex"


file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserCreateVipPaymentTransaction.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-PaymentGatewayCallbackVerification.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-PaymentSuccessUpdateOutbox.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-PaymentOutboxRelayKafka.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-PaymentSendVipConfirmationEmail.tex"
file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserTransactionHistoryLookup.tex"


# file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserVoiceLiveKitToken.tex"
# file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserVoiceChatWithAi.tex"
# file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserUploadPersonalDocument.tex"
# file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-DocumentWorkerProcessDocument.tex"
# file_path = r"C:\Users\Admin\Documents\GitHub\docs-latex\latex\contents\Sequence\UML-Sequence-UserAnalyzePersonalDocumentRag.tex"


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

        # Ghi lại nội dung đã thay thế vào file
        with open(path, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"Đã xử lý và lưu thành công file:\n{path}")

    except FileNotFoundError:
        print(f"Lỗi: Không tìm thấy file tại đường dẫn {path}")
    except Exception as e:
        print(f"Đã xảy ra lỗi: {e}")


# Chạy hàm xử lý
process_latex_file(file_path)
