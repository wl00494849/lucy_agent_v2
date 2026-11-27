import httpx
import logging
from langchain.tools import tool
from src.agents.tools.schema import DockerAction
from src.core.config import settings
class Dockerd():
    def __int__(self):
        self.dockerd_url = settings.DOCKERD_HOST
        
    @tool()
    async def dockerd_images_list(self):
        """
        Call the internal Docker API to retrieve images data.
        """
        async with httpx.AsyncClient(timeout=10,verify=False) as client:
            try:
                respones = await client.get(url=self.dockerd_url + "images")
                return respones.json()
            except Exception as exc:
                print(exc)

    @tool()
    async def dockerd_containers_list(self):
        """
        Call the internal Docker API to retrieve containers data.
        """
        async with httpx.AsyncClient(timeout=10,verify=False) as client:
            try:
                respones = await client.get(url=self.dockerd_url + "containers")
                return respones.json()
            except Exception as exc:
                logging.exception(exc)


    @tool(args_schema=DockerAction)
    async def dockerd_start_container(
            self,
            container_id:str,
            tags:str
        ):
        async with httpx.AsyncClient(timeout=10,verify=False) as client:
            try:
                respones = await client.post(
                    url=self.dockerd_url + "start",
                    json={
                        "image_id":container_id,
                        "tags":tags
                    }
                )

                return respones.json()

            except Exception as exc:
                logging.exception(exc)

    @tool(args_schema=DockerAction)
    async def dockerd_stop_container(
            self,
            container_id:str,
            tags:str
        ):
        async with httpx.AsyncClient(timeout=10,verify=False) as client:
            try:
                respones = await client.post(
                    url=self.dockerd_url + "stop",
                    json={
                        "image_id":container_id,
                        "tags":tags
                    }
                )

                return respones.json()

            except Exception as exc:
                logging.exception(exc)