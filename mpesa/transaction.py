import requests
from requests.auth import HTTPBasicAuth
import datetime
import base64



consumer_key = "u8FTVGviqOprRT5Ehn3zyn70K6FLykFJ"
consumer_secret = "KLH5hYwGxZcEYcKz"
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

access_token = r.json()['access_token']

api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

headers = { "Authorization": "Bearer %s" % access_token }

passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"


short_code = "174379"


def mpesa_push(PhoneNumber,name,desc,id):
  timestamp = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
  p = short_code+passkey+timestamp
  password = base64.b64encode(p.encode(), altchars=None).decode()
  request = {
    "BusinessShortCode": short_code,
    "Password": password,
    "Timestamp": timestamp,
    "TransactionType": "CustomerPayBillOnline",
    "Amount": "1",
    "PartyA": PhoneNumber,
    "PartyB": short_code,
    "PhoneNumber": PhoneNumber,
    "CallBackURL": "https://eabd938d.ngrok.io/mpesa/callback/{}".format(id),
    "AccountReference": name,
    "TransactionDesc": desc
  }
  response = requests.post(api_url, json = request, headers=headers)
  print (response.text)
  return response.text

#transaction('254729446214','daniel')
if __name__=='__main__':
  pass
