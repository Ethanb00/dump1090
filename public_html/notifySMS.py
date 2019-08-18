import twilio
from twilio.rest import Client
from conf import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TO_PHONE, FROM_PHONE
account_sid = TWILIO_ACCOUNT_SID
auth_token = TWILIO_AUTH_TOKEN
client = Client(account_sid, auth_token)
print(TWILIO_ACCOUNT_SID)
message = client.messages \
                .create(
                     body="An aircraft overhead is transmitting an emergency squawk code.",
                     from_=FROM_PHONE,
                     to=TO_PHONE
                 )

#print(message.sid)