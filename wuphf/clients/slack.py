
import os
import logging
from slackclient import SlackClient
from .. import wuphf

log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class Slack(wuphf.Client):
	"""docstring for Slack."""
	def __init__(self):
		# super(Slack, self).__init__()
		self.client = SlackClient(os.getenv('WUPHF_SLACK_API_TOKEN'))

	def format(self, message, tag_channel=False):
		msg = f'*{message.title}*\n{message.body}'

		if tag_channel:
			msg.append('\n<!channel>')
		return msg

	def _format_send_to(self, send_to):
		for i in range(len(send_to)):
			print(send_to[i])
			if '#' not in send_to[i]:
				send_to[i] = f'#{send_to[i]}'
		return send_to

	def send(self, message, send_to):
		message, send_to = super(Slack, self).send(message, send_to)

		send_to = self._format_send_to(send_to)
		msg = self.format(message)

		for channel in send_to:
			self.client.api_call(
					"chat.postMessage",
					channel=channel,
					text=msg,
					username='Alfred',
					as_user=True
			)
