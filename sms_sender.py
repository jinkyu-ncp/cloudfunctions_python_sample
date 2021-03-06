import urllib.parse
import urllib.request
import ssl
import json

# REST End-point
API_HOST = 'https://api-sens.ncloud.com'
# NCP Access Key ID
AUTH_KEY = 'qEvQEqjALeNxsOXqAa0F'
# SENS project name
PROJECT_NAME = 'first_project'
# SENS service id
SERVICE_ID = 'ncp:sms:kr:253463679625:first_project'
# SENS project secret key
SERVICE_SECRET = '62f008b56cde420a9408ba38a9f7350b'
# Request URL
FULL_PATH = API_HOST + '/v1/sms/services/' + SERVICE_ID + '/messages'
# Request Body
data = {
  "type": "sms",
  "contentType": "comm",
  "countryCode": "82",
  "from": "0100000000",
  "to": [
    "0100000000"
  ],
  "content": "hello world"
}


class SmsSender:

    @staticmethod
    def req_sms():
        context = ssl._create_unverified_context()

        req = urllib.request.Request(FULL_PATH)

        req.add_header('X-NCP-auth-key', AUTH_KEY)
        req.add_header('X-NCP-service-secret', SERVICE_SECRET)
        req.add_header('Content-Type', 'application/json')

        json_data = json.dumps(data)
        json_data_bytes = json_data.encode('utf-8')

        response = urllib.request.urlopen(req, json_data_bytes, context=context)

        return response