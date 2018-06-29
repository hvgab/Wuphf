import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import COMMASPACE, formatdate
from email import encoders

import logging
import pprint
# from time import sleep
# import re
from operator import itemgetter
# from slugify import slugify
# import fnmatch

from .. import wuphf

""" SMTP_CLIENT """

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())

pp = pprint.PrettyPrinter()

class SMTP(wuphf.Client):
	""" docstring for SMTP_Client. """

	def __init__(self):
		log.debug('SMTP Client init')
		# super(SMTP_Client, self).__init__()
		self.server=os.getenv('WUPHF_SMTP_SERVER')
		self.port=os.getenv('WUPHF_SMTP_PORT')
		self.username=os.getenv('WUPHF_SMTP_USERNAME')
		self.password=os.getenv('WUPHF_SMTP_PASSWORD')
		self.send_from=os.getenv('WUPHF_SMTP_SEND_FROM')
		self.tls=os.getenv('WUPHF_SMTP_TLS')
		log.debug('SMTP Client init')

	def format(self, message, send_to, cc):
		""" Format message object """
		# not implemented, format function could create html message?
		html = False

		log.debug('smtp format')
		if message.files is None:
			files = []
		if message.images is None:
			message.images = []

		# create smtp message
		msg = MIMEMultipart('related')
		msg['From'] = self.send_from
		if send_to is not None:
			msg['To'] = COMMASPACE.join(send_to)
		msg['Date'] = formatdate(localtime=True)
		msg['Subject'] = message.title

		print(cc)
		print(type(cc))
		if cc is not None:
			msg['CC'] = COMMASPACE.join(cc)

		msg.attach( MIMEText(message.body, 'html' if html else 'plain') )

		if message.files is not None:
			for f in message.files:
				part = MIMEBase('application', "octet-stream")
				part.set_payload( open(f,"rb").read() )
				Encoders.encode_base64(part)
				part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
				msg.attach(part)

		if message.images is not None:
			for (n, i) in enumerate(message.images):
				fp = open(i, 'rb')
				msgImage = MIMEImage(fp.read())
				fp.close()
				msgImage.add_header('Content-ID', '<image{0}>'.format(str(n+1)))
				msg.attach(msgImage)

		return msg

	def send(self, message, send_to, cc=None):
		""" Send message

			Args:
				msg = wuphf.Message object
				to = list-like with email adresses
			Return:
				True/False
				# TODO: Make a wuphf response object?
		"""

		log.debug('SMTP send')

		# Send to has to be list-like
		send_to = send_to if isinstance(send_to, list) else [send_to]
		if cc is not None:
			cc = cc if isinstance(cc, list) else [cc]

		msg = self.format(message, send_to, cc)

		smtp = smtplib.SMTP(host=self.server, port=int(self.port))
		smtp.set_debuglevel(False)

		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login(self.username, self.password)
		to_addrs = []
		to_addrs.extend(send_to)
		if cc is not None:
			to_addrs.extend(cc)
		log.debug('to_addrs: \n\t{}'.format(to_addrs))
		smtp.sendmail(self.send_from, to_addrs, msg.as_string())
		print('SEND MAIL\t{subject} sent to {mail_to}, cc {mail_to_cc}'.format(subject=msg['Subject'], mail_to=msg['To'], mail_to_cc=msg['CC']))
		smtp.close()
		log.info('Message sent')
