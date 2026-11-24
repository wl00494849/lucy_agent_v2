from pydantic_settings import BaseSettings,SettingsConfigDict
from sqlalchemy.engine import URL
from functools import lru_cache

class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    OPENAI_API_KEY:str
    PORT:int

    #SQL
    DRIVER:str = "postgresql"
    PSQL_USER:str
    PSQL_PASSWORD:str
    PSQL_HOSTNAME:str
    PSQL_PORT:str
    PSQL_DB_NAME:str

    #REDIS
    REDIS_HOST:str
    REDIS_PORT:int

    #API
    DOCKERD_HOST:str

    @property
    def postgresql_url(self)->URL:
        return URL.create(
            drivername=self.DRIVER,
            username=self.PSQL_USER,
            password=self.PSQL_PASSWORD,
            host=self.PSQL_HOSTNAME,
            port=self.PSQL_PORT,
            database=self.PSQL_DB_NAME
        )

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()