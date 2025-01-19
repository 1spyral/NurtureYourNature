from openai import OpenAI

# Initialize OpenAI client
client = OpenAI(api_key="")

# Create assistants and threads
therapist_assistant = client.beta.assistants.create(
    name="Therapist",
    instructions="You are a trendy therapist disguised as a friend that is trying to dig deep into the user's psyche and provide them with the best advice possible. Only respond with 20 words or less.",
    model="gpt-4-turbo-preview"
)

health_assistant = client.beta.assistants.create(
    name="Health Monitor",
    instructions="You are responsible for determining whether the user is taking care of their health or not. You can only respond with 'yes', 'no', 'unknown'.",
    model="gpt-4-turbo-preview"
)

therapist_thread = client.beta.threads.create()
health_thread = client.beta.threads.create()

def generate(prompt):
    
    return generate_persona1(prompt), generate_persona2(prompt)

def generate_persona1(prompt):
    # Add message to therapist thread
    message = client.beta.threads.messages.create(
        thread_id=therapist_thread.id,
        role="user",
        content=prompt
    )
    
    # Run the assistant
    run = client.beta.threads.runs.create(
        thread_id=therapist_thread.id,
        assistant_id=therapist_assistant.id
    )
    
    # Wait for completion
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(
            thread_id=therapist_thread.id,
            run_id=run.id
        )
    
    # Get the latest message
    messages = client.beta.threads.messages.list(thread_id=therapist_thread.id)
    return messages.data[0].content[0].text.value

def generate_persona2(prompt):
    # Add message to health thread
    message = client.beta.threads.messages.create(
        thread_id=health_thread.id,
        role="user",
        content=prompt
    )
    
    # Run the assistant
    run = client.beta.threads.runs.create(
        thread_id=health_thread.id,
        assistant_id=health_assistant.id
    )
    
    # Wait for completion
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(
            thread_id=health_thread.id,
            run_id=run.id
        )
    
    # Get the latest message
    messages = client.beta.threads.messages.list(thread_id=health_thread.id)
    return messages.data[0].content[0].text.value