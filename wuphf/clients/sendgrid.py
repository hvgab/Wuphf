import logging
import os

import sendgrid
from sendgrid.helpers.mail import *

from .. import wuphf

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class Sendgrid(wuphf.Client):
    """docstring for sendgrid_client."""

    def __init__(self):
        # super(sendgrid_client, self).__init__()
        self.apikey = os.getenv('WUPHF_SENDGRID_API_TOKEN')
        log.debug(f'apikey {self.apikey}')
        self.sg = sendgrid.SendGridAPIClient(apikey=self.apikey)

    def format(self, message, send_to):
        """ Builds a Sendgrid Mail object """
        from_email = Email(os.getenv('WUPHF_SENDGRID_FROM'))
        to_email = [Email(_) for _ in send_to]
        subject = message.title
        content = Content("text/plain", message.body)
        mail = Mail(from_email, subject, to_email.pop(0), content)
        for addr in to_email:
            mail.personalizations[0].add_to(addr)
        return mail.get()

    def send(self, message, send_to):
        """ Sends the sendgrid mail object """
        msg = self.format(message, send_to)
        response = self.sg.client.mail.send.post(request_body=msg)
        log.debug(response.status_code)
        log.debug(response.body)
        log.debug(response.headers)
