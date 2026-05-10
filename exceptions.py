from fastapi import status

from constants.exception_constants import (
    INVALID_REQUEST_MESSAGE,
    NOT_FOUND_EXCEPTION_MESSAGE,
    UNAUTHENTICATED_EXCEPTION_MESSAGE,
    ALREADY_EXISTS_EXCEPTION_MESSAGE,
    UNAUTHORIZED_EXCEPTION_MESSAGE,
    JWT_GENERATION_EXCEPTION_MESSAGE,
    UNSUPPORTED_FILE_EXCEPTION_MESSAGE,
    LARGE_FILE_EXCEPTION_MESSAGE
)
class BaseException(Exception):
    def __init__(self, message):
        super().__init__(message)


class UnAutenticatedException(BaseException):
    def __init__(self, message=UNAUTHENTICATED_EXCEPTION_MESSAGE):
        self.status_code = status.HTTP_401_UNAUTHORIZED
        super().__init__(message)

class UnAuthorizedException(BaseException):
    def __init__(self, message = UNAUTHORIZED_EXCEPTION_MESSAGE):
        self.status_code = status.HTTP_403_FORBIDDEN
        super().__init__(message)

class InvalidRequestException(BaseException):
    def __init__(self, message=INVALID_REQUEST_MESSAGE):
        self.status_code = status.HTTP_422_UNPROCESSABLE_CONTENT
        super().__init__(message)

class NotFoundException(BaseException):
    def __init__(self, message=NOT_FOUND_EXCEPTION_MESSAGE):
        self.status_code = status.HTTP_404_NOT_FOUND
        super().__init__(message)

class AlreadyExistsException(BaseException):
    def __init__(self, message=ALREADY_EXISTS_EXCEPTION_MESSAGE):
        self.status_code = status.HTTP_409_CONFLICT        
        super().__init__(message)

class JWTGenerationException(BaseException):
    def __init__(self, message=JWT_GENERATION_EXCEPTION_MESSAGE):
        self.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        super().__init__(message)

class UnSupportedFileException(BaseException):
    def __init__(self, message=UNSUPPORTED_FILE_EXCEPTION_MESSAGE):
        self.status_code = status.HTTP_415_UNSUPPORTED_MEDIA_TYPE
        super().__init__(message)

class LargeFileException(BaseException):
    def __init__(self, message=LARGE_FILE_EXCEPTION_MESSAGE):
        self.status_code = status.HTTP_413_CONTENT_TOO_LARGE
        super().__init__(message)