import logging

import chromalog
import wuphf
from test_config import MAIL_01, MAIL_02

chromalog.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

log.debug('start create client')
w = wuphf.clients.Sendgrid()
log.debug('end create client')

log.debug('start create message')
msg = wuphf.Message('Test Title', 'Test Body')
log.debug('end create message')

log.debug('start send')
w.send(msg, [MAIL_01, MAIL_02])
log.debug('end send')
