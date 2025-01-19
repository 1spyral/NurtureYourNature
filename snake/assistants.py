

import os
from dotenv import load_dotenv, set_key, find_dotenv
from tools.ai_service import ai_client

from pydantic import BaseModel
from enum import Enum
import json

class RoboOutput(str, Enum):
    good = "GOOD"
    bad = "BAD"
    unknown = "UNKNOWN"

class OutputSchema(BaseModel):
    message: str
    healthy: RoboOutput


# Create assistants and threads
therapist_assistant = ai_client.beta.assistants.create(
    name="Therapist",
    instructions="""
You are a trendy therapist disguised as a friend that is trying to dig deep into the user's psyche and provide them with the best advice possible. 
Only respond with 20 words or less. 
Additionally, assess the user's lifestyle decisions and give GOOD, BAD, or UNKNOWN for neutral. For example, going on a walk would be GOOD. While sleeping in would be BAD.

Your output format will follow a JSON structure. Always respond with just a JSON structure

{
    "message": string,
    "lifestyle": string
}
""",
    model="gpt-4o-mini",
)

health_assistant = ai_client.beta.assistants.create(
    name="Health Monitor",
    instructions="You are responsible for determining whether the user is taking care of their health or not. You can only respond with 'yes', 'no', 'unknown'.",
    model="gpt-4o-mini"
)

if __name__ == "__main__":
    # Load existing .env file
    dotenv_path = find_dotenv()
    load_dotenv()

    # Function to update or create environment variables
    def update_env_variable(key, value):
        if os.getenv(key) != value:
            set_key(dotenv_path, key, value)

    # Update or create THERAPIST_ID and HEALTH_ID
    update_env_variable('THERAPIST_ID', therapist_assistant.id)
    update_env_variable('HEALTH_ID', health_assistant.id)

