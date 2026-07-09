from langchain_openai import ChatOpenAI
import os

class LangChainChat():
    def __init__(self,model:str="gpt-4.1-mini"):
        self.client = ChatOpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            model=model,
            temperature=0.3
        )

    def request(self,prompt:str):
        
        pass
    
    