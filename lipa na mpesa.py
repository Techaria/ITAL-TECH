import base64
from datetime import datetime

import requests
import keys


# unformated_time = datetime.now()
# formatted_time = unformated_time.strftime("%Y%m%d%H%M%S")


# data_to_encode = keys.business_shortCode + keys.lipa_na_mpesa_passkey + formatted_time
# encoded_string = base64.b64encode(data_to_encode.encode())

# decoded_password = encoded_string.decode('utf-8')
# # print(decoded_password)
# print(encoded_string)
# print(formatted_time)

from requests.auth import HTTPBasicAuth

consumer_key = keys.consumer_key
consumer_secret = keys.consumer_secrete
api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

print (r.text) 
# json_response = r.json()
# access_token = json_response['access_token']


# def lipa_na_mpesa():

# 	access_token = access_token
# 	api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequst"
# 	headers = {"Authorization":"Bearer %s" % access_token}
# 	request = {
# 		"BusinessShortCode":keys.business_shortCode,
# 		"Password":decoded_password,
# 		"Timestamp": formatted_time,
# 		"TransactionType":"CustomerPayBillOnline",
# 		"Amout":"1",
# 		"PartyA":keys.phone_number,
# 		"PartyB":keys.business_shortCode,
# 		"PhoneNumber":keys.phone_number,
# 		"CallBackURL":"https://http://127.0.0.1:8000/callback",
# 		"AccountReference":"36796086",
# 		"TransactionDesc":"Lipa to UCIPS",

# 	}

# 	response = requests.post(api_url,json=request,headers=headers)

# 	print(response.txt)

