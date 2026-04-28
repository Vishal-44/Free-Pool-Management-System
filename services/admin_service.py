from exceptions import AlreadyExistsException, NotFoundException
from repositories.admin_repository import AdminRepository
from serializers.admin import EmployeeOnboardRequest, EmployeeOnboardResponse
from constants.response_constants import EMPLOYEE_ALREADY_EXISTS_MESSAGE, DESIGNATION_NOT_FOUND_MESSAGE
from utils.password_utils import generate_random_password

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