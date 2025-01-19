from tools.ai_service import ai_client
from collections import deque
from config import THERAPIST_ID, HEALTH_ID

class Thread:
    def __init__(self):
        self.messages = deque([])
        self.id = ai_client.beta.threads.create().id

    def create(self, prompt, role = "user"):
        ai_client.beta.threads.messages.create(
            self.id,
            content=prompt,
            role=role
        )
        self.messages.appendleft({
            "role": role,
            "content": prompt
        })

    def run(self, type = 1): # 1 - therapist    2 - health
        if type == 1:
            assistant_id = THERAPIST_ID
        else:
            assistant_id = HEALTH_ID
        
        ai_client.beta.threads.runs.create_and_poll(
            thread_id=self.id,
            assistant_id=assistant_id
        )

        messages = ai_client.beta.threads.messages.list(thread_id=self.id)

        message = messages.data[0].content[0].text.value

        self.messages.appendleft({
            "role": "assistant",
            "content": message
        })

        print(self.messages)

        return messages.data[0].content[0]

    def get_messages(self):
        return self.messages