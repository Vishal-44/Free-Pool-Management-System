from starlette.middleware.base import BaseHTTPMiddleware

from configs.midldleware_config import authenticaion_registry
from constants.middleware_constant import (
    CONFIGURED_AUTH_SERVICE,
    UNAUTHENTICATED_ENDPOINTS
)

class AuthenticationMiddleware(BaseHTTPMiddleware):

    def __init__(self, app):
        super().__init__(app)
        self.authentication_registry = authenticaion_registry
        self.configured_auth_service = CONFIGURED_AUTH_SERVICE
        self.unauthenticated_endpoints = UNAUTHENTICATED_ENDPOINTS
    

    def get_auth_service(self):
        return self.authentication_registry.get(self.configured_auth_service, None)
    

    def should_skip_authentication(self, request):
        return request.url.path in self.unauthenticated_endpoints


    async def dispatch(self, request, call_next):
        if self.should_skip_authentication(request):
            return await call_next(request)
        
        auth_service = self.get_auth_service()

        is_authenticated, error_response = auth_service.authenticate(request)

        if not is_authenticated:
            return error_response

        return await call_next(request)

    