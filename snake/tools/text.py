from tools.twilio_service import twilio_client
from config import TO, FROM

def text(message):
    twilio_client.messages.create(
        body=message,
        to=TO,
        from_=FROM
    )
