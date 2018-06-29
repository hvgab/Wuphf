
import requests
import json
import os
import logging
from .. import wuphf


log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class Purecloud(wuphf.Client):
	""" Purecloud Wuphf Client

		Send message to group
	"""

	def __init__(self):
		# super(Purecloudwuphf.client, self).__init__()
		pass

	def format(self, message):
		""" Format message """
		message = f'**{message.title}**\n{message.body}'
		return message

	def format_send_to(self, send_to):
		""" Format send to """
		if isinstance(send_to, (list, tuple)):
			send_to = ' '.join(send_to)
			return send_to
		elif isinstance(send_to, str):
			return send_to
		else:
			raise ValueError('Purecloud send_to has to be list or string')

	def send(self, message, send_to):
		""" Send message """
		message = self.format(message)
		send_to = self.format_send_to(send_to)

		payload = {
				'message':message,
				'metadata':send_to}

		log.debug('payload\n\t',json.dumps(payload))

		r = requests.post(os.getenv('WUPHF_PURECLOUD_WEBHOOK_URL'), data=json.dumps(payload))

		log.debug(f'statuscode: {r.status_code}')
		log.debug(f'inin id: {r.headers["inin-correlation-id"]}')
		log.debug(f'headers: {r.headers}')
