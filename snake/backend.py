from fastapi import FastAPI, Form, Query
from contextlib import asynccontextmanager
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from twilio.twiml.voice_response import VoiceResponse
from twilio.twiml.messaging_response import MessagingResponse
from apiRouter import apiRouter
from plant import plant
from tools.text import text

app = FastAPI()

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting server...")
    prompt = "Hello! How was your day?"
    id = plant.new()
    plant.create(id, prompt, "assistant")
    text(prompt)
    yield
    print("Shutting down server...")

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your needs
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(apiRouter)

@app.post("/start")
async def start():
    prompt = "Hello! How was your day?"
    id = plant.new()
    plant.create(id, prompt, "assistant")
    response = VoiceResponse()
    response.say(prompt)
    response.gather(input="speech", action=f"/user_response?id={id}")
    return HTMLResponse(str(response))

@app.post("/user_response")
async def user_response(SpeechResult: str = Form(None), id: int = Query(None)):
    print(SpeechResult)
    response = VoiceResponse()

    # Check for speech input
    if SpeechResult:
        speech = SpeechResult.lower() 
        plant.create(id, speech)
        response.say(plant.run(id).text.value)
        response.gather(input="speech", action=f"/user_response?id={id}")
    else:
        response.say("Sorry, I didn't hear anything. Ending the call...")
        response.hangup()

    return HTMLResponse(str(response))

@app.post("/sms")
async def sms_reply(Body: str = Form(None), From: str = Form(None)):
    if Body and From:
        print(f"Received SMS from {From}: {Body}")
    else:
        print("Missing required data in request.")

    plant.create(0, Body)

    response = MessagingResponse()

    response.message(plant.run(0).text.value)

    return HTMLResponse(str(response))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend:app", host="127.0.0.1", port=8000, reload=True)
