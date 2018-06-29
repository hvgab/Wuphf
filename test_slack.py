import logging

import chromalog
import wuphf
from test_config import SLACK_CHANNEL

chromalog.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

log.debug('start create client')
w = wuphf.clients.Slack()
log.debug('end create client')

log.debug('start create message')
msg = wuphf.Message('Test Title', 'Test Body')
log.debug('end create message')

log.debug('send_to string')
w.send(msg, f'#{SLACK_CHANNEL}')

log.debug('send_to list')
w.send(msg, [f'#{SLACK_CHANNEL}'])

log.debug('send_to tuple')
w.send(msg, (f'#{SLACK_CHANNEL}'))

#  NO HASH
log.debug('send_to string no hash')
w.send(msg, SLACK_CHANNEL)

log.debug('send_to list no hash')
w.send(msg, [SLACK_CHANNEL])

log.debug('send_to tuple no hash')
w.send(msg, (SLACK_CHANNEL))
