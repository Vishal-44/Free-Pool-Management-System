from authentication_services.jwt_authentication_service import JWTAuthenticationService
from exceptions import NotFoundException, UnAuthorizedException
from repositories.auth_repository import AuthRepository
from serializers.auth import AuthRequest
from serializers.response import APIResponse
from utils.auth_utils import validate_payload

class AuthService:
    
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AuthService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        self.auth_service = JWTAuthenticationService()
        self.auth_repository = AuthRepository()

    def generate_token(self, payload):
        return self.auth_service.create_jwt_token(payload)
    
    def login(self, body: AuthRequest):
        validate_payload(body)

        admin = self.auth_repository.is_admin(body)
        if not admin:
            raise NotFoundException("Admin not found with the provided credentials")
        
        match = admin.password == body.password
        if not match:
            raise UnAuthorizedException("Invalid credentials: Incorrect password")

        token_payload = {"admin_info": body.username or body.email}
        token = self.generate_token(token_payload)
        return APIResponse(
            message="Login successful",
            data={"token": token}
        )