from typing import Literal
from pydantic import BaseModel, Field

class DockerAction(BaseModel):
    """
    Start or Stop Docker container
    """
    container_id:str = Field(description="Container ID")
    action: Literal["start","stop"]= Field(description="Docker action")
