from fastapi import APIRouter, Query
from plant import plant

apiRouter = APIRouter()

@apiRouter.get("/api/chats")
async def get_chats():
    return plant.get_chats()

@apiRouter.get("/api/chat")
async def get_chat(chatId: str = Query(None)):
    return plant.threads[int(chatId)].get_messages()