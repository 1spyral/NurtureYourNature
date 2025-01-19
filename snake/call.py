from tools.twilio_service import twilio_client
from config import TO, FROM, ML_HOST

def call():
    print(TO)
    call = twilio_client.calls.create(
        to=TO,
        from_=FROM,
        url=ML_HOST + "/start"
    )

    print(call.sid)

if __name__ == "__main__":
    call()