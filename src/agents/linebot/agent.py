from langchain.agents import create_agent
from langchain_openai import ChatOpenAI 
from src.core.config import settings

class LineBotAgent():
    def __init__(
            self,
            system_prompt:str = None,
            model:str="gpt-4.1-mini"
        ):
        self._langchain_llm = ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model=model,
            timeout=30,
            max_retries=3,
            temperature=0.3,
        )

        self.agent = create_agent(
            model=self._langchain_llm,
            system_prompt=system_prompt
        )

    def invoke(self,prompt:str)->str:

        msg = {
            "messages": [
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        }

        result = self.agent.invoke(msg)
        response = result["messages"][-1].content
        return response