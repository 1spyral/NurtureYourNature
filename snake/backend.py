from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from twilio.twiml.voice_response import VoiceResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/start")
async def start():
    response = VoiceResponse()
    response.say("Hello. Press 1 or 2.")
    response.gather(input="speech", num_digits=1, action="/user_response")
    return HTMLResponse(str(response))

@app.post("/user_response")
async def user_response(SpeechResult: str = Form(None)):
    print(SpeechResult)
    response = VoiceResponse()

    # Check for speech input
    if SpeechResult:
        speech = SpeechResult.lower()  # Normalize speech result (e.g., "exit")
        if "exit" in speech:
            response.say("Thank you for calling. Goodbye!")
            response.hangup()
        else:
            response.say(f"You said: {speech}. Press 1 for more options or say 'exit' to end the call.")
            response.gather(input="speech", num_digits=1, action="/user_response")
    
    else:
        response.say("Sorry, I didn't get that. Please press 1 for a fun fact, or say 'exit' to end the call.")
        response.gather(input="speech", num_digits=1, action="/user_response")

    return HTMLResponse(str(response))