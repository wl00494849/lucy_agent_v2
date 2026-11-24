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

    def redis_set(self,):
        self.client.set()
        pass

    def redis_get(self):
        self.client.get()
        pass

    def redis_delete(self):
        self.client.delete()
        pass

    def redis_eval(self):
        self.client.eval()
        pass
