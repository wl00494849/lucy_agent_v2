from langchain.agents import create_agent
from langchain_openai import ChatOpenAI 

class LineBotAgent():
    def __init__(self,model:str="gpt-4.1-mini"):
        self._langchain_llm = ChatOpenAI(
            api_key=self._api_key,
            model=model,
            timeout=30,
            max_retries=3,
            temperature=0.3,
        )
        
        self.agent = create_agent(
            model=self._langchain_llm,
        )

    def invoke(self,prompt:str):
        pass