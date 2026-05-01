from fastapi import APIRouter, status, Request
from fastapi.responses import JSONResponse

from serializers.admin import EmployeeOnboardRequest
from serializers.response import APIResponse
from services.admin_service import AdminService
from middlewares.authorization import requires_admin_role
from constants.response_constants import EMPLOYEE_ONBOARD_SUCCESS_MESSAGE

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

admin_service = AdminService()

@router.post("/employees", response_model=APIResponse)
@requires_admin_role()
async def onboard_employee(request: Request, payload: EmployeeOnboardRequest):
    onboard_response = admin_service.onboard_employee(payload)
    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content=APIResponse(
            message=EMPLOYEE_ONBOARD_SUCCESS_MESSAGE,
            data=onboard_response.model_dump()
        ).model_dump()
    )
