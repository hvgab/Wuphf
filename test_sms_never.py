import logging

import chromalog
import wuphf
from test_config import SMS_01

chromalog.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

log.debug('start create message')
msg = wuphf.Message('Test Title', 'Test Body')
log.debug('end create message')

log.debug('start create client')
w = wuphf.clients.SMS_never()
log.debug('end create client')

log.debug('send_to string')
w.send(msg, SMS_01)

log.debug('send_to list')
w.send(msg, [SMS_01])

log.debug('send_to tuple')
w.send(msg, (SMS_01))

#
# #  NO HASH
# log.debug('send_to string no hash')
# w.send(msg, 'test')
#
# log.debug('send_to list no hash')
# w.send(msg, ['test'])
#
# log.debug('send_to tuple no hash')
# w.send(msg, ('test'))
