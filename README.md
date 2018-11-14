
# WUPHF

Send a message to a person on all platforms, WUPHF!

Made to easyily send notifications from cron-like to IT and non-IT employees.

## Quickstart

```python
from wuphf import Wuphf, Msg

wuphf = Wuphf()

msg = Msg(title='title', msg='message'))

wuphf.slack(msg, ('#my-channel'))
# or
wuphf.send(msg, ('#my-channel'), 'slack')

```

## Services:

- SMTP (mail)
- Sendgrid (mail)
- Purecloud
- Slack
- MS Teams
- DRSSMS (corp sms service)
