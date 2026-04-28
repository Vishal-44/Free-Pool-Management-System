from configs.midldleware_config import authenticaion_registry
from serializers.auth import AuthRequest
from exceptions import InvalidRequestException
from constants.middleware_constant import (
    CONFIGURED_AUTH_SERVICE
)
from constants.exception_constants import (
    AUTH_SERVICE_NOT_CONFIGURED_MESSAGE
)

def validate_payload(payload: AuthRequest):
    if not payload.username and not payload.email:
        raise InvalidRequestException("Either username or email must be provided.")

def get_auth_header(payload: dict):
    auth_service = get_configured_auth_service()
    return auth_service.create_auth_headers(payload=payload)

def get_configured_auth_service():
    auth_service = authenticaion_registry.get(CONFIGURED_AUTH_SERVICE, None)
    if not auth_service:
        raise Exception(AUTH_SERVICE_NOT_CONFIGURED_MESSAGE)
    return auth_service