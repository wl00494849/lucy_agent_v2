from redis import Redis,ConnectionPool,Connection
from src.core.config import settings

class RedisClient():
    def __init__(self,db:int=0):
        self.client = Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            db=db,
            max_connections=5,
            health_check_interval=60,
        )

    def ping(self):
        self.ping()
        print("Redis connect success")

    def redis_set(self,val:any,key:str):
        self.client.set(name=key,value=val)
        pass

    def redis_get(self,key:str):
        self.client.get(key)
        pass

    def redis_delete(self,key:str):
        self.client.delete(key)
        pass
    
    def redis_rpush(self,key:str,val:any):
        pass

    def redis_lpush(self,key:str,val:any):
        pass

    def redis_eval(self):
        pass
