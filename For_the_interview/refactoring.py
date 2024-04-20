import smtplib
import imaplib
from email import message_from_string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

if __name__ == '__main__':
    class Gmail:
        def __init__(self, login: str, password: str) -> None:
            self.GMAIL_SMTP = "smtp.gmail.com"
            self.GMAIL_IMAP = "imap.gmail.com"

            self.login = login
            self.password = password

        def send_message(self, recipients: list,
                         subject: str, message: str) -> None:
            msg = MIMEMultipart()
            msg['From'] = self.login
            msg['To'] = ', '.join(recipients)
            msg['Subject'] = subject
            msg.attach(MIMEText(message))

            ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
            ms.ehlo()
            ms.starttls()
            ms.ehlo()

            ms.login(self.login, self.password)
            ms.sendmail(self.login, ms, msg.as_string())

            ms.quit()

        def receive_message(self, header=None):
            mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)

            mail.login(self.login, self.password)
            mail.list()
            mail.select('inbox')
            criterion = '(HEADER Subject "%s)' % header if header else 'ALL'
            result, data = mail.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = message_from_string(raw_email)

            mail.logout()

            return email_message


    gmail_session = Gmail(login='login@gmail.com', password='qwerty')

    recipients = ['vasya@email.com', 'petya@email.com']
    subject = 'Subject'
    message = 'Message'

    send = gmail_session.send_message(recipients, subject, message)
    last_message = gmail_session.receive_message()
