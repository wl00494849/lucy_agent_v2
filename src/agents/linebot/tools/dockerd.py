import httpx
from typing import Literal
from src.core.config import settings
from pydantic import BaseModel

async def dockerd_info(cmd:Literal["containers","images"]):
    async with httpx.AsyncClient(timeout=10,verify=False) as client:
        try:
            respones = await client.get(url=settings.DOCKER_HOST + cmd)
            respones.json()
        except Exception as exc:
            print(exc)

async def dockerd_exec(
        cmd:Literal["start","stop"],
        image_id:str,
        tags:str
    ):
    async with httpx.AsyncClient(timeout=10,verify=False) as client:
        try:
            respones = await client.post(
                url=settings.DOCKER_HOST + cmd,
                json={
                    "image_id":image_id,
                    "tags":tags
                }
            )
            respones.json()

        except Exception as exc:
            pass