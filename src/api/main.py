from fastapi import APIRouter
from src.api.api_v1 import (
    linebot,
    system
)

router = APIRouter()

router.include_router(linebot.router,
                      prefix="/linebot",
                      tags=["LineBot"])
router.include_router(system.router,
                      prefix="/system",
                      tags=["System"])