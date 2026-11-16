from pydantic import BaseModel

class LineBotRequest(BaseModel):
    uid:str
    prompt:str