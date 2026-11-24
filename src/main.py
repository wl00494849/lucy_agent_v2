from fastapi import FastAPI
from src.api.main import router
from src.core.config import settings

app = FastAPI()
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app=app,
        port=settings.PORT,
)