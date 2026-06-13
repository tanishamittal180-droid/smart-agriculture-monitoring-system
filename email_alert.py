import smtplib
from email.message import EmailMessage


class EmailAlert:

    def send_alert(
        self,
        sender_email,
        sender_password,
        receiver_email,
        subject,
        message
    ):

        email = EmailMessage()

        email["Subject"] = subject

        email["From"] = sender_email

        email["To"] = receiver_email

        email.set_content(message)

        with smtplib.SMTP_SSL(
            "smtp.gmail.com",
            465
        ) as smtp:

            smtp.login(
                sender_email,
                sender_password
            )

            smtp.send_message(email)