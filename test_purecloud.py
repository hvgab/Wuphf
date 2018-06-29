import logging

import chromalog
import test_config
import wuphf

chromalog.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

log.debug('start create message')
msg = wuphf.Message('Test Title', 'Test Body')
log.debug('end create message')

log.debug('start create client')
w = wuphf.clients.Purecloud()
log.debug('end create client')

# HASHTAG
log.debug('send_to string')
w.send(msg, f'#{test_config.PURECLOUD_CHANNEL}')

log.debug('send_to list')
w.send(msg, [f'#{test_config.PURECLOUD_CHANNEL}'])

log.debug('send_to tuple')
w.send(msg, (f'#{test_config.PURECLOUD_CHANNEL}'))

#  NO HASHTAG
log.debug('send_to string no hash')
w.send(msg, f'{test_config.PURECLOUD_CHANNEL}')

log.debug('send_to list no hash')
w.send(msg, [f'{test_config.PURECLOUD_CHANNEL}'])

log.debug('send_to tuple no hash')
w.send(msg, (f'{test_config.PURECLOUD_CHANNEL}'))
