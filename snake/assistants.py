import os
from dotenv import load_dotenv, set_key, find_dotenv
from tools.ai_service import client

# Create assistants and threads
therapist_assistant = client.beta.assistants.create(
    name="Therapist",
    instructions="You are a trendy therapist disguised as a friend that is trying to dig deep into the user's psyche and provide them with the best advice possible. Only respond with 20 words or less.",
    model="gpt-4o-mini"
)

health_assistant = client.beta.assistants.create(
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

