from authentication_services.jwt_authentication_service import JWTAuthenticationService
from exceptions import NotFoundException, UnAutenticatedException
from repositories.auth_repository import AuthRepository
from serializers.auth import (
    AuthRequest, 
    EmployeeLoginRequest
)
from serializers.response import APIResponse
from utils.auth_utils import (
    validate_payload, 
    get_auth_header
)
from utils.password_utils import verify_password

class AuthService:
    
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AuthService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.auth_service = JWTAuthenticationService()
        self.auth_repository = AuthRepository()
    
    
    def login(self, body: AuthRequest):
        validate_payload(body)

        admin = self.auth_repository.is_admin(body)
        if not admin:
            raise NotFoundException("Admin not found with the provided credentials")
        
        match = admin.password == body.password
        if not match:
            raise UnAutenticatedException("Invalid credentials: Incorrect password")

        admin_data = {"email": admin.email}
        auth_headers = get_auth_header(payload=admin_data)
        
        return APIResponse(
            message="Login successful"
        ), auth_headers
    
    def employee_login(self, body: EmployeeLoginRequest):

        employee = self.auth_repository.is_employee(body)

        if not employee:
            raise NotFoundException("Admin not found with the provided credentials")
        
        if not verify_password(body.password, employee.password):
            raise UnAutenticatedException("Invalid credentials: Incorrect password.")
        
        employee_data = {"email": employee.email}
        auth_headers = get_auth_header(payload=employee_data)

        return APIResponse(
            message = "Login successfully"
        ), auth_headers