from fastapi import APIRouter, status, Request
from fastapi.responses import JSONResponse

from serializers.admin import EmployeeOnboardRequest
from serializers.response import APIResponse
from services.admin_service import AdminService
from middlewares.authorization import requires_admin_role
from constants.response_constants import EMPLOYEE_ONBOARD_SUCCESS_MESSAGE, EMPLOYEE_SEARCH_SUCCESS_MESSAGE
from exceptions import InvalidRequestException
from constants.exception_constants import MISSING_QUERY_PARAM_MESSAGE

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

admin_service = AdminService()

@router.get("/employees/search", response_model=APIResponse)
@requires_admin_role()
async def search_employees(
    request: Request,
    query: str | None = None,
    page: int = 1,
    page_size: int = 10
):
    if query is None:
        raise InvalidRequestException(MISSING_QUERY_PARAM_MESSAGE)
    
    result = admin_service.search_employees(query, page, page_size)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=APIResponse(
            message=EMPLOYEE_SEARCH_SUCCESS_MESSAGE,
            data=result.model_dump()
        ).model_dump()
    )

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
