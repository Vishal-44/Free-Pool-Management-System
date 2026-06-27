from fastapi import APIRouter, Query, Request
from fastapi import status as fastapi_status
from fastapi.responses import JSONResponse

from serializers.admin import EmployeeOnboardRequest
from serializers.response import APIResponse
from services.admin_service import AdminService
from middlewares.authorization import requires_admin_role
from storage_services.types import EmployeeStatus
from constants.response_constants import (
    EMPLOYEE_LIST_SUCCESS_MESSAGE,
    EMPLOYEE_ONBOARD_SUCCESS_MESSAGE,
    EMPLOYEE_SEARCH_SUCCESS_MESSAGE,
    SKILL_LIST_SUCCESS_MESSAGE,
)
from exceptions import InvalidRequestException
from constants.exception_constants import (
    INVALID_PAGINATION_MESSAGE,
    MISSING_QUERY_PARAM_MESSAGE,
)

router = APIRouter(
    prefix="/admin",
    tags=["admin"]
)

admin_service = AdminService()

@router.get("/skills", response_model=APIResponse)
async def list_skills(
    domain: str | None = None,
    page: int = 1,
    page_size: int = 10,
):
    if page < 1 or page_size < 1:
        raise InvalidRequestException(INVALID_PAGINATION_MESSAGE)

    result = admin_service.list_skills(
        domain=domain,
        page=page,
        page_size=page_size,
    )
    return JSONResponse(
        status_code=fastapi_status.HTTP_200_OK,
        content=APIResponse(
            message=SKILL_LIST_SUCCESS_MESSAGE,
            data=result.model_dump()
        ).model_dump()
    )

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
        status_code=fastapi_status.HTTP_200_OK,
        content=APIResponse(
            message=EMPLOYEE_SEARCH_SUCCESS_MESSAGE,
            data=result.model_dump()
        ).model_dump()
    )

@router.get("/employees", response_model=APIResponse)
@requires_admin_role()
async def list_employees(
    request: Request,
    status: EmployeeStatus | None = None,
    department: str | None = None,
    designation: str | None = None,
    skill: list[str] | None = Query(default=None),
    page: int = 1,
    page_size: int = 10,
):
    if page < 1 or page_size < 1:
        raise InvalidRequestException(INVALID_PAGINATION_MESSAGE)

    result = admin_service.list_employees(
        status=status,
        department=department,
        designation=designation,
        skill=skill,
        page=page,
        page_size=page_size,
    )
    return JSONResponse(
        status_code=fastapi_status.HTTP_200_OK,
        content=APIResponse(
            message=EMPLOYEE_LIST_SUCCESS_MESSAGE,
            data=result.model_dump()
        ).model_dump()
    )

@router.post("/employees", response_model=APIResponse)
@requires_admin_role()
async def onboard_employee(request: Request, payload: EmployeeOnboardRequest):
    onboard_response = admin_service.onboard_employee(payload)
    return JSONResponse(
        status_code=fastapi_status.HTTP_201_CREATED,
        content=APIResponse(
            message=EMPLOYEE_ONBOARD_SUCCESS_MESSAGE,
            data=onboard_response.model_dump()
        ).model_dump()
    )
