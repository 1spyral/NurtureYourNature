from twilio.rest import Client
from config import ACCOUNT_SID, TWILIO_TOKEN, TO, FROM, ML_HOST

client = Client(ACCOUNT_SID, TWILIO_TOKEN)

print("Twilio client initialized")

def call():
    call = client.calls.create(
        to=TO,
        from_=FROM,
        url=ML_HOST + "/start"
    )

    print(call.sid)

if __name__ == "__main__":
    call()