from openai import OpenAI
from src.core.config import settings
import os

class OpenAIChat():
    def __init__(
            self,
            model:str = "gpt-4.1-mini"
        ):
        self._api_key = settings.OPENAI_API_KEY
        self.client = OpenAI(api_key=self._api_key)
        self.model = model

    def get_vector(self,text:str,is_big_size:bool=False):
        model = "text-embedding-3-small"
        if is_big_size == True:
            model = "text-embedding-3-large"
        
        response = self.client.embeddings.create(
            model=model,
            input=text
        )

        vector = response.data
        return vector

    def request(self,prompt:str,model:str=None)->str:
        use_model = self.model
        if model != None:
            use_model = model

        response = self.client.responses.create(
            model=use_model,
            prompt=prompt
        )

        text = response.output_text
        return text