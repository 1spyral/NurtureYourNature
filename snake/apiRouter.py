from fastapi import APIRouter

apiRouter = APIRouter()

@apiRouter.get("chats")
async def get_chats():
    return 