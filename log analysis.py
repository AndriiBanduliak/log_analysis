import smtplib
from email.mime.text import MIMEText

FILE = 'error.log'
SERVER = 'smtp.yandex.ru'
PORT = 587
LOGIN = '************'
PASSWORD = '*********'

TO = '*********gmail.com'
FROM_EMAIL = '**********'
TEXT_TYPE = 'html'


def check_error(file):
    f = open(file, 'r')
    lines = f.readlines()
    f.close()
    notice = 0
    warnings = 0
    errors = 0
    for line in lines:
        if '[php7:notice]' in line:
            notice += 1
        elif '[php7:warn]' in line:
            warnings += 1
        elif '[php7:error]' in line:
            errors += 1
    if notice or warnings or errors:
        send_report(notice, warnings, errors)


def send_report(notice, warnings, errors):
    message = "<div>Типы ошибок и их количество</br >"
    message += "<b>Notices:</b>" + str(notice) + "<br />"
    message += "<b>Warnings:</b>" + str(warnings) + "<br />"
    message += "<b>Errors:</b>" + str(errors) + "</ div>"
    send_email(' ', 'Есть ошибки', message)


def send_email(to, subject, message):
    msg = MIMEText(message, TEXT_TYPE, 'utf-8')
    msg['Subject'] = subject
    msg['From'] = FROM_EMAIL
    msg['To'] = to

    smtp = smtplib.SMTP(SERVER, PORT)
    smtp.starttls()
    smtp.login(LOGIN, PASSWORD)
    smtp.send_message(msg)
    smtp.quit()


if __name__ == "__main__":
    check_error(FILE)