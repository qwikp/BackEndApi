import urllib.request
import uuid

import requests, datetime

from . models import SMSLog

_USER = 'InstaDerm'
_HASH = 'b96b02dff4be80c6280b3f7c98ff434aa5a19d56'
_URL = 'https://sms.intime.nu/api/1.0/message/create.ashx' + '?user=' + _USER + '&hash=' + _HASH


def send_sms(phone_no, message, user=None, title=None):
    title = title or phone_no
    uid = str(uuid.uuid4())

    data1 = f"""<?xml version="1.0" encoding="iso-8859-1"?>
        <message>
        <flash>0</flash>
        <multisms>0</multisms>
        <senddate>{datetime.datetime.now()}</senddate>
        <sendertitle>Vaccina</sendertitle>
        <body>{message}</body>
        <recipients>
            <recipient transid="{uid}">{phone_no}</recipient>
        </recipients>
        </message>
    """

    req = urllib.request.Request(_URL, data=str.encode(data1), headers={'Content-Type': 'text/xml'})
    response = urllib.request.urlopen(req)
    print(response.read())
    SMSLog.objects.create(**{
        'user': user,
        'phone_no': phone_no,
        'message': message,
        'transaction_id': uid,
        'server_message_id': response.read().decode('utf-8'),
        'last_status': 'sent',
    })


def send_sms_v2(phone_no, message):
    url = "https://http-api.d7networks.com/send"
    querystring = {
        "username":"yjks4247",
        "password":"HUVY2hYx",
        "from":"QuikPharma",
        "content": message,
        "dlr-method":"POST",
        "dlr-url":"https://4ba60af1.ngrok.io/receive",
        "dlr":"yes",
        "dlr-level":"3",
        "to": phone_no
    }
    headers = {
        'cache-control': "no-cache"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)