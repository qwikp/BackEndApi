import urllib.request
import uuid

from . models import SMSLog

_USER = 'InstaDerm'
_HASH = 'b96b02dff4be80c6280b3f7c98ff434aa5a19d56'
_URL = 'https://sms.intime.nu/api/1.0/message/create.ashx' + '?user=' + _USER + '&hash=' + _HASH


def send_sms(phone_no, message, user=None, title=None):
    title = title or phone_no
    uid = str(uuid.uuid4())
    data = """<?xml version="1.0" encoding="iso-8859-1"?>
    <message>
        <flash>0</flash>
        <multisms>1</multisms>
        <sendertitle>""" + title + """</sendertitle>
        <body>""" + message + """</body>
        <recipients>
            <recipient transid=\"""" + uid + """\">""" + phone_no + """</recipient>
        </recipients>
    </message>"""

    req = urllib.request.Request(_URL, data=str.encode(data), headers={'Content-Type': 'text/xml'})
    response = urllib.request.urlopen(req)
    SMSLog.objects.create(**{
        'user': user,
        'phone_no': phone_no,
        'message': message,
        'transaction_id': uid,
        'server_message_id': response.read().decode('utf-8'),
        'last_status': 'sent',
    })