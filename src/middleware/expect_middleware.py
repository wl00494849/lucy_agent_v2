from collections.abc import Callable
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse,Response
import logging

class ExceptionMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self,request:Request,call_next:Callable)->Response:
        try:

            response = await call_next(request)
            return response
    
        except Exception as exc:
            logging.exception(f"Unexcept Error : {exc}")
            return JSONResponse(
                status_code=500,
                content={"detail":"500 Internal Server Error"}
            )