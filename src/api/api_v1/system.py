from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/live")
async def live():
    try:
        return JSONResponse(
            content="ok",
            status_code=200
        )
    except Exception as exc:
        print(exc)