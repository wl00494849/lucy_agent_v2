from fastapi import APIRouter
from src.api.schemas.linebot import LineBotRequest
from src.agents.linebot.agent import LineBotAgent
import httpx

router = APIRouter()

@router.get("/linebot-agent")
async def linebot_agent(param:LineBotRequest):
    agent = LineBotAgent()
    response = agent.ainvoke(prompt=param.prompt)
    return response
