import logging
import os

from drssms import NeverAPI

from .. import wuphf

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class SMS_never(wuphf.Client):
    """ send sms via never """

    def __init__(self):
        # super(SMS_never, self).__init__()
        self.sms = NeverAPI()
        self.sms.login()
        self.send_from = 'WUPHF@DRS'

    def format(self, message):
        return f'{message.title}\n\n{message.body}'

    def format_send_to(self, send_to):
        if isinstance(send_to, str):
            return [int(send_to)]
        elif isinstance(send_to, list):
            return send_to
        else:
            raise ValueError('')

    def send(self, message, send_to):
        if not isinstance(send_to, list):
            log.error('send_to has to be list')
            return

        message = self.format(message)

        for number in send_to:
            self.sms.send_push_sms(number, message, ani=self.send_from)
            log.info(f'Sms sent to {number}')
