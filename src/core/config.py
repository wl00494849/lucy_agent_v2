from pydantic_settings import BaseSettings,SettingsConfigDict

class Settings(BaseSettings):
    OPENAI_API_KEY:str
    POSTGRESQL_URL:str
    PORT:int

settings = Settings()