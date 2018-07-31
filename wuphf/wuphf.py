import logging

import wuphf

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class Contact(object):
    """ Wuphf Contact """

    def __init__(self,
                 name,
                 mail=None,
                 sms=None,
                 purecloud_channel=None,
                 slack_channel=None):
        # super(Contact, self).__init__()
        self.name = name
        self.mail = mail
        self.sms = sms
        self.purecloud_channel = purecloud_channel
        self.slack_channel = slack_channel


class Message(object):
    """ Message class

		Create a message once and send it with any client.
		Client should format this as it seems fit.
	"""

    def __init__(self, title, body, files=None, images=None):
        self.title = title
        self.body = body
        self.files = files
        self.images = images


class Client(object):
    """ Messaging client """

    def __init__(self):
        raise NotImplementedError('Subclass must define this func.')

    def send(self, message, send_to):
        """ Send message """
        log.debug('super send')

        if isinstance(send_to, str):
            send_to = [send_to]

        assert isinstance(send_to, list)

        return message, send_to
        # raise NotImplementedError('Subclass must define this func.')


class Wuphf(object):
    """ The wuphf class """

    def __init__(self):
        log.debug('start Wuphf init')
        self.smtp = wuphf.clients.SMTP()
        self.sendgrid = wuphf.clients.Sendgrid()
        self.slack = wuphf.clients.Slack()
        self.purecloud = wuphf.clients.Purecloud()
        self.sms = wuphf.clients.SMS_never()

    def smtp(self, message, send_to):
        log.debug('start send smtp')
        self.smtp.send(message, send_to)
        log.debug('end send smtp')

    def sendgrid(self, message, send_to):
        log.debug('start send sendgrid')
        self.sendgrid.send(message, send_to)
        log.debug('end send sendgrid')

    def slack(self, message, send_to):
        self.slack.send(message, send_to)

    def purecloud(self, message, send_to):
        self.purecloud.send(message, send_to)

    def sms(self, message, send_to):
        self.sms_never.send(message, send_to)

    def send(self, message, contacts):
        """ Send to multiple channel at the same time.

			Args:
				msg
				send_to: wuphf.Contact
		"""

        # TODO: Formater tekst 1 gang hvis lista er for lang

        for contact in contacts:
            self.mail(message, contact.mail)
            self.sms(message, contact.sms)
            self.purecloud(message, contact.purecloud_channel)
            self.slack(message, contact.slack_channel)
