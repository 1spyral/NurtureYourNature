from twilio.rest import Client
from config import ACCOUNT_SID, TWILIO_TOKEN

twilio_client = Client(ACCOUNT_SID, TWILIO_TOKEN)

print("Twilio client initialized")

