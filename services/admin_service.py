from exceptions import AlreadyExistsException, NotFoundException
from repositories.admin_repository import AdminRepository
from serializers.admin import (
    EmployeeListResponse, EmployeeOnboardRequest, EmployeeOnboardResponse,
    EmployeeSearchResponse, SkillItem, SkillListResponse,
)
from constants.response_constants import EMPLOYEE_ALREADY_EXISTS_MESSAGE, DESIGNATION_NOT_FOUND_MESSAGE
from storage_services.types import EmployeeStatus
from utils.password_utils import generate_random_password
from utils.employee_utils import to_employee_list_item, to_employee_search_result

class AdminService:

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AdminService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.admin_repository = AdminRepository()

    def onboard_employee(self, payload: EmployeeOnboardRequest) -> EmployeeOnboardResponse:
        existing_employee = self.admin_repository.get_employee_by_email(payload.email)
        if existing_employee:
            raise AlreadyExistsException(EMPLOYEE_ALREADY_EXISTS_MESSAGE)
        
        designation = self.admin_repository.get_designation_by_name(payload.designation)
        if not designation:
            raise NotFoundException(DESIGNATION_NOT_FOUND_MESSAGE)
        
        generated_password, hashed_password = generate_random_password()
        employee = self.admin_repository.create_employee(payload, hashed_password, designation)
        
        return EmployeeOnboardResponse(
            email=employee.email,
            password=generated_password
        )

    def search_employees(self, query: str, page: int, page_size: int) -> EmployeeSearchResponse:
        total, employees = self.admin_repository.search_employees(query, page, page_size)
        items = [to_employee_search_result(e) for e in employees]
        return EmployeeSearchResponse(total=total, page=page, page_size=page_size, items=items)

    def list_employees(
        self,
        status: EmployeeStatus | None,
        department: str | None,
        designation: str | None,
        skill: list[str] | None,
        page: int,
        page_size: int,
    ) -> EmployeeListResponse:
        skills = [s for s in skill if s] if skill else None

        total, employees = self.admin_repository.list_employees(
            status=status,
            department=department,
            designation=designation,
            skills=skills,
            page=page,
            page_size=page_size,
        )
        items = [to_employee_list_item(e) for e in employees]
        return EmployeeListResponse(total=total, page=page, page_size=page_size, items=items)

    def list_skills(
        self,
        domain: str | None,
        page: int,
        page_size: int,
    ) -> SkillListResponse:
        total, skills = self.admin_repository.list_skills(
            domain=domain,
            page=page,
            page_size=page_size,
        )
        items = [
            SkillItem(id=skill.id, name=skill.name, domain=skill.domain)
            for skill in skills
        ]
        return SkillListResponse(total=total, page=page, page_size=page_size, items=items)
