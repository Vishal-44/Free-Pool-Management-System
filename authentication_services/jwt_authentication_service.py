import os
from jose import jwt, JWTError
from fastapi.responses import JSONResponse
from datetime import datetime, timezone, timedelta

from authentication_services.base_auth_service import BaseAuthService
from constants.exception_constants import (
    INTERNAL_SERVER_ERROR_MESSAGE,
    MISSING_HEADER_EXCEPTION_MESSAGE, 
    MISSING_JWT_TOKEN_EXCEPTION_MESSAGE
)
from exceptions import (
    UnAuthorizedException,
    JWTGenerationException
)

class JWTAuthenticationService(BaseAuthService):
    _intance = None
    def __new__(cls, *args, **kwargs):
        if cls._intance is None:
            cls._intance = super(JWTAuthenticationService, cls).__new__(cls, *args, **kwargs)
        return cls._intance

    def __init__(self):
        self.jwt_secret_key = os.getenv("JWT_SECRET_KEY", None)
        self.jwt_algorithm = os.getenv("JWT_ALGORITHM", "HS256")
        self.jwt_expiry = int(os.getenv("JWT_EXPIRY", "3600"))

        if not self.jwt_secret_key:
            raise ValueError("JWT_SECRET_KEY is not configured in environment variables.")
    

    def create_jwt_token(self, payload: dict) -> str:
        """
        Generate a signed JWT token.
 
        Args:
            payload: Arbitrary claims to embed in the token
                     (e.g. {"sub": user_id, "role": "admin"}).
 
        Returns:
            A signed JWT string.
        """
        try: 
            now = datetime.now(tz=timezone.utc)
            claims = {
                **payload,
                "iat": now,                                          # issued-at
                "exp": now + timedelta(seconds=self.jwt_expiry),    # expiry
            }
            token = jwt.encode(claims, self.jwt_secret_key, algorithm=self.jwt_algorithm)
        except JWTError as e:
            raise JWTGenerationException()
        return token
    
    
    @staticmethod
    def _extract_jwt_token(request):

        authentication_header = request.headers.get("Authorization", None)
        if authentication_header is None or not authentication_header.startswith("Bearer "):
            raise UnAuthorizedException(message = MISSING_HEADER_EXCEPTION_MESSAGE)
        
        token = authentication_header[7:].strip()

        if not token:
            raise UnAuthorizedException(message = MISSING_JWT_TOKEN_EXCEPTION_MESSAGE)
        
        return token
    

    def validate_jwt_token(self, token):
        try:
            claims = jwt.decode(
                token,
                self.jwt_secret_key,
                algorithms=[self.jwt_algorithm]
            )
            return claims
        
        except JWTError as e:
            print(str(e))
            raise UnAuthorizedException()

    
    def authenticate(self, request):
        try:
            token = self._extract_jwt_token(request)
            claims = self.validate_jwt_token(token)
            request.state.user_claims = claims
            return True, None
        
        except Exception as e:
            
            if isinstance(e, UnAuthorizedException):
                return False, JSONResponse(
                    status_code=e.status_code,
                    content={
                        "message": str(e)
                    }
            )
            print(str(e))
            return False, JSONResponse(
                status_code=500,
                content={
                    "message": INTERNAL_SERVER_ERROR_MESSAGE
                }
            )
            