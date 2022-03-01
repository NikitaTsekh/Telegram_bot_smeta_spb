import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import config.config


# Отправка письма на почту
def send_email(email, document):
    sender = config.config.SENDER
    receiver = config.config.RECEIVER
    password = config.config.SENDER_PASSWORD

    # Создание подключения
    server = smtplib.SMTP('smtp.yandex.ru', 587)
    #587  у яндекса у гугла почта
    server.ehlo()
    server.starttls()

    try:
        message = MIMEMultipart()
        message["From"] = sender
        message["Subject"] = "Новое обращение"
        message.attach(MIMEText(email))

        # Если есть приложение
        if document != 0:
            # Прикрепление файла
            part = MIMEApplication(
                document.file_id,
                Name=document.file_name
            )
            part['Content-Disposition'] = 'attachment; filename="%s"' % document.file_name
            message.attach(part)

        server.login(sender, password)
        server.sendmail(sender, receiver, message.as_string())
        server.quit()
        return "Message done"
    except Exception as e:
        server.quit()
        return f"{e}"


