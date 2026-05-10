from fastapi import UploadFile
from storage_services.file_upload_service import FileUploadService
from serializers.employee import Skills
from utils.json_utils import convert_to_json
from repositories.employee_repository import EmployeeRepository
from serializers.response import APIResponse
from constants.response_constants import EMPLOYEE_PROFILE_UPDATED_MESSAGE

class EmployeeService():
    def __init__(self):
        self.file_upload_service = FileUploadService()
        self.employee_repository = EmployeeRepository()

    async def update_profile(self, email: str, description: str, skills: str, profile_picture: UploadFile = None):
        url = None
        if profile_picture:
            url = await self.file_upload_service.upload(file=profile_picture)
        skills = [Skills(**skill) for skill in convert_to_json(skills)] if skills else []
        self.employee_repository.update_employee(email = email, description = description, skills = skills, image_url = url)
        return APIResponse(
            message = EMPLOYEE_PROFILE_UPDATED_MESSAGE,
        )
