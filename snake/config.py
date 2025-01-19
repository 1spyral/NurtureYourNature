import os
from dotenv import load_dotenv

load_dotenv()

ACCOUNT_SID = os.getenv("ACCOUNT_SID")
TWILIO_TOKEN = os.getenv("TWILIO_TOKEN")
TO = os.getenv("TO")
FROM = os.getenv("FROM")
ML_HOST = os.getenv("ML_HOST")

OPENAI_TOKEN = os.getenv("OPENAI_TOKEN")

THERAPIST_ID = os.getenv("THERAPIST_ID")
HEALTH_ID = os.getenv("HEALTH_ID")