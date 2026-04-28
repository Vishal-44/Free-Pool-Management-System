from authentication_services.jwt_authentication_service import JWTAuthenticationService
from exceptions import NotFoundException, UnAuthorizedException
from repositories.auth_repository import AuthRepository
from serializers.auth import AuthRequest
from serializers.response import APIResponse
from utils.auth_utils import (
    validate_payload, 
    get_auth_header
)

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
            raise UnAuthorizedException("Invalid credentials: Incorrect password")

        admin_data = {"id": admin.id, "email": admin.email}
        auth_headers = get_auth_header(payload=admin_data)
        
        return APIResponse(
            message="Login successful"
        ), auth_headers