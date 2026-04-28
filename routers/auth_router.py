from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from serializers.auth import AuthRequest
from serializers.response import APIResponse
from services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

auth_service = AuthService()

@router.post("/login", response_model=APIResponse)
async def login(payload: AuthRequest):
    response = auth_service.login(payload)
    return JSONResponse(
        status_code = status.HTTP_200_OK,
        content = response.model_dump()
    )