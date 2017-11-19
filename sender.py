
import abc

import smtplib
from email.mime.text import MIMEText


class Sender(abc.ABC):

    @abc.abstractmethod
    def format_message(self, message):
        pass

    @abc.abstractmethod
    def send(self, sender_from, sender_to, message):
        pass


class TemplateFormatMixin:

    def __init__(self, **kwargs):
        self.template = kwargs.pop('template', None)
        template_file = kwargs.pop('template_file', None)
        if not self.template and not template_file:
            raise ValueError('A template or a template file must be provided')

        if not self.template and template_file:
            with open(template_file) as tf:
                self.template = tf.read()

    @classmethod
    def read_template_from_file(self, path):
        with open(path) as f:
            return f.read()

    def format_message(self, sender_from, sender_to):
        return self.template.format(sfrom=sender_from, sto=sender_to)


class EmailSender(TemplateFormatMixin, Sender):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.config = kwargs.pop('email_config')
        self.server = None

    def setup_server(self):
        server = smtplib.SMTP(self.config.get('host'), self.config.get('port', 587))
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.config.get('username'), self.config.get('password'))
        self.server = server

    def format_message(self, secret_from, secret_to):
        message = super().format_message(secret_from, secret_to)
        sender = (self.config.get('sender_name'), self.config.get('sender_email'))

        email = MIMEText(message, 'html')
        email['From'] = '{} <{}>'.format(*sender)
        email['To'] = '{to.name} <{to.email}>'.format(to=secret_from)
        email['Subject'] = self.config.get('subject')
        return email

    def send(self, secret_from, secret_to, message):
        if self.server is None:
            self.setup_server()
        from_addr = self.config.get('sender_email')
        self.server.sendmail(from_addr, secret_from.email, message.as_string())


class ConsoleSender(TemplateFormatMixin, Sender):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def send(self, secret_from, secret_to, message):
        print(message)
