import cv2
import numpy as np
import datetime
#CloudantDB
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey
import requests
#Provide CloudantDB credentials such as username,password and url
client = Cloudant("bf65b7a1-9773-40f8-af7d-d6de14cfbc49-bluemix", "e3892dc34d2cd565bbee23d67f7d3402bb9fae944b947e38133da849cdb19bb3", url="https://bf65b7a1-9773-40f8-af7d-d6de14cfbc49-bluemix:e3892dc34d2cd565bbee23d67f7d3402bb9fae944b947e38133da849cdb19bb3@bf65b7a1-9773-40f8-af7d-d6de14cfbc49-bluemix.cloudantnosqldb.appdomain.cloud")
client.connect()
#Provide your database name
database_name ="smartwastemanagement"
my_database = client.create_database(database_name)
if my_database.exists():
   print(f"'{database_name}' successfully created.")
url = "https://www.fast2sms.com/dev/bulk"
querystring = {"authorization":"OVoIJEXZ2jF5yitCn07g4ULmK1GY8HWhk3fcwPvAurdbzeqSDNLWmIFQYuk6hsqBRKndH5GzPS1DwX92","sender_id":"FSTSMS","message":"This dustbin is full","language":"english","route":"p","numbers":"9398099056,8978307614,7337220205,9100209787"}
headers = {
    'cache-control': "no-cache"
}
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
