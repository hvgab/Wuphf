import logging

import chromalog
import wuphf
from test_config import MAIL_01

chromalog.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

log.debug('start create client')
w = wuphf.Wuphf()
log.debug('end create client')

log.debug('start create message')
msg = wuphf.Message('Test Title', 'Test Body')
log.debug('end create message')

log.debug('start send')
w.smtp(msg, (MAIL_01))
log.debug('end send')
