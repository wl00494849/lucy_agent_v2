from fastapi import APIRouter
from src.api.schemas.linebot import LineBotRequest
import httpx

router = APIRouter()

@router.get("/linebot-agent")
async def linebot_agent(param:LineBotRequest):
    async with httpx.AsyncClient(timeout=10,verify=False) as client:
        pass
        
    