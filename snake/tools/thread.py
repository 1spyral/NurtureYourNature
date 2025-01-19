from tools.ai_service import client
from collections import deque
from config import THERAPIST_ID, HEALTH_ID

class Thread:
    def __init__(self):
        self.messages = deque([])
        self.id = client.beta.threads.create().id

    def create(self, prompt):
        self.messages.appendleft({
            "role": "user",
            "content": prompt
        })

    def run(self, type = 1): # 1 - therapist    2 - health
        if type == 1:
            assistant_id = THERAPIST_ID
        else:
            assistant_id = HEALTH_ID
        
        client.beta.threads.runs.create_and_poll(
            thread_id=self.id,
            assistant_id=assistant_id
        )

        messages = client.beta.threads.messages.list(thread_id=self.id)

        message = messages.data[0].content[0].text.value

        self.messages.appendleft({
            "role": "assistant",
            "content": message
        })

        return message

    def get_messages(self):
        return self.messages