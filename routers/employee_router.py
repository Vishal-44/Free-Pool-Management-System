from fastapi import APIRouter, Request, status, Form, UploadFile, File
from fastapi.responses import JSONResponse
from typing import Optional

from middlewares.authorization import requires_employee_role
from services.employee_service import EmployeeService
from serializers.response import (
    APIResponse
)

router = APIRouter(
    prefix="/employee",
    tags=["Employee"]
)

employee_service = EmployeeService()

@router.put("/update-profile", response_model = APIResponse)
@requires_employee_role()
async def update_employee(
    request: Request,
    description: Optional[str]  = Form(default = None),
    skills: Optional[str] =  Form(default = None),
    profile_image : Optional[UploadFile] = File(default = None)
): 
    email = request.state.user.get("email")
    response = await employee_service.update_profile(
        email = email, 
        description = description, 
        skills = skills, 
        profile_picture = profile_image
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content = response.model_dump()
    )