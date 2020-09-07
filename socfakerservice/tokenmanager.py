import secrets
from socfakerservice import mail
from flask_mail import Message
from .config import Config
from .words import funny_words


class TokenManager:

    __subject = 'soc-faker: Requested API Token'
    __sender = Config().MAIL_USERNAME
    __text_body = '''
Thank you for requesting an API token for soc-faker.

Your Requested API Token is: {token}

If you received this message and did not expect to, please create an issue in your GitHub repository: https://github.com/MSAdministrator/soc-faker-service

Thank you,

MSAdministrator
'''

    __html_body = '''
<h1>Thank you for requesting an API token for soc-faker.</h1>

Your Requested API Token is: <b>{token}</b>

If you received this message and did not expect to, please create an issue in your GitHub repository: <a href="https://github.com/MSAdministrator/socfakerservice">https://github.com/MSAdministrator/socfakerservice</a>

Thank you,

<a href="https://github.com/MSAdministrator">MSAdministrator</a>
'''
    __token = None

    def __init__(self, email_address):
        self.email = email_address

    @property
    def token(self):
        if not self.__token:
            words = [word.strip() for word in funny_words]
            self.__token = ''.join(secrets.choice(words).capitalize() for i in range(6))
        return self.__token

    def send_email(self):
        try:
            msg = Message(self.__subject, sender=self.__sender, recipients=[self.email])
            msg.body = self.__text_body.format(token=self.token)
            msg.html = self.__html_body.format(token=self.token)
            mail.send(msg)
        except:
            pass
           # print(msg, flush=True)
           # print(f"Sending email to {self.email} containing new token: {self.token}", flush=True)
           # print(f"The entire message is:\n{msg}")
