from fastapi import FastAPI
from src.api.main import router
from src.core.config import settings
from src.middleware.expect_middleware import ExceptionMiddleware

app = FastAPI()
linebot_app = FastAPI()

# router
app.include_router(router)

# middleware
app.add_middleware(ExceptionMiddleware)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app=app,
        port=settings.PORT,
)