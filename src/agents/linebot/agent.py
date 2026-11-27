from langchain.agents import create_agent
from langchain_openai import ChatOpenAI 
from src.core.config import settings
from src.agents.tools.dockerd import Dockerd
from src.agents.tools.google_tool import GoogleTool

class LineBotAgent():
    def __init__(
            self,
            system_prompt:str = None,
            model:str="gpt-6.1-terra"
        ):
        _dockerd = Dockerd()
        _google = GoogleTool()

        self.TOOL = [
            _dockerd.dockerd_images_list,
            _dockerd.dockerd_containers_list,
            _dockerd.dockerd_start_container,
            _dockerd.dockerd_stop_container,
        ]

        self._langchain_llm = ChatOpenAI(
            api_key=settings.OPENAI_API_KEY,
            model=model,
            timeout=30,
            max_retries=3,
            temperature=0.3,
        )

        self._agent = create_agent(
            model=self._langchain_llm,
            system_prompt=system_prompt,
            tools=self.TOOL
        )

    def ainvoke(self,prompt:str)->str:

        msg = {
            "messages": [
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        }

        result = self._agent.invoke(msg)
        response = result["messages"][-1].content
        return response