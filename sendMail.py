from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import Config


def send_email(addr_to, msg_text):
    addr_from = Config.addr_from
    password = Config.password

    msg = MIMEMultipart()
    msg['From'] = addr_from
    msg['To'] = addr_to
    msg['Subject'] = "Кто-то задал вам вопрос!"

    msg.attach(MIMEText(msg_text, 'plain'))

    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.set_debuglevel(True)
    server.login(addr_from, password)
    server.send_message(msg)
    server.quit()

