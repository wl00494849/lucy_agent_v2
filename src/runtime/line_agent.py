from src.infrastructure.llms.langchain_client import LangChainChat

class LineAgent():
    def __init__(self):
        self.chat = LangChainChat()
    
    def agent(self,prompt:str)->str:
        memory = []
        
