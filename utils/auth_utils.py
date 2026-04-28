from serializers.auth import AuthRequest
from exceptions import InvalidRequestException

def validate_payload(payload: AuthRequest):
    if not payload.username and not payload.email:
        raise InvalidRequestException("Either username or email must be provided.")