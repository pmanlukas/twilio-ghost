import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         #body='+491709296197: Sure',
         body='Hey, I need a Taxi to munich central station, cheers Lukas',
         from_='+17372103868',
         #to='+491709296197'
         to='+16672072802'
     )

print(message.sid)