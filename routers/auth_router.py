from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

from serializers.auth import AuthRequest, EmployeeLoginRequest
from serializers.response import APIResponse
from services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

auth_service = AuthService()

@router.post("/login", response_model=APIResponse)
async def login(body: AuthRequest):
    response, auth_headers = auth_service.login(body)
    return JSONResponse(
        status_code = status.HTTP_200_OK,
        content = response.model_dump(),
        headers = auth_headers
    )

@router.post("/employee/login", response_model=APIResponse)
async def employee_login(body: EmployeeLoginRequest):
    response, auth_headers = auth_service.employee_login(body)
    return JSONResponse(
        status_code = status.HTTP_200_OK,
        content = response.model_dump(),
        headers = auth_headers
    )