from smtplib import SMTP_SSL, SMTPException
from email.message import EmailMessage
from ssl import SSLContext
import datetime


def find_next_sunday() -> str:
    _today = datetime.date.today()

    # Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday
    # 1       2        3          4         5       6         7

    if _today.isoweekday() == 1:
        _today_delta = datetime.timedelta(days=6)
        _today = _today + _today_delta
        return f"{_today.month}/{_today.day}/{_today.year}"
    elif _today.isoweekday() == 2:
        _today_delta = datetime.timedelta(days=5)
        _today = _today + _today_delta
        return f"{_today.month}/{_today.day}/{_today.year}"
    elif _today.isoweekday() == 3:
        _today_delta = datetime.timedelta(days=4)
        _today = _today + _today_delta
        return f"{_today.month}/{_today.day}/{_today.year}"
    elif _today.isoweekday() == 4:
        _today_delta = datetime.timedelta(days=3)
        _today = _today + _today_delta
        return f"{_today.month}/{_today.day}/{_today.year}"
    elif _today.isoweekday() == 5:
        _today_delta = datetime.timedelta(days=2)
        _today = _today + _today_delta
        return f"{_today.month}/{_today.day}/{_today.year}"
    elif _today.isoweekday() == 6:
        _today_delta = datetime.timedelta(days=1)
        _today = _today + _today_delta
        return f"{_today.month}/{_today.day}/{_today.year}"
    elif _today.isoweekday() == 7:
        return f"{_today.month}/{_today.day}/{_today.year}"


def make_EmailMessage(_to: str, _from: str, subject: str, body: str) -> EmailMessage:
    email_message = EmailMessage()
    email_message["To"] = _to
    email_message["From"] = _from
    email_message["Subject"] = subject
    email_message.set_content(body)

    return email_message


def send_email(
    email: str, password: str, recipient: str, msg: EmailMessage, context: SSLContext
):
    try:
        with SMTP_SSL("smtp.gmail.com", port=465, context=context) as smtp:
            smtp.login(user=email, password=password)
            smtp.sendmail(email, recipient, msg.as_string())
    except SMTPException as e:
        print("Something went wrong when trying to send email.")
        print(f"Error: {e}")

