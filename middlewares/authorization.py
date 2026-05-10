from functools import wraps
from exceptions import UnAuthorizedException 

from repositories.auth_repository import AuthRepository
from serializers.auth import AuthRequest, EmployeeLoginRequest

auth_repository = AuthRepository()


def requires_admin_role():

    def decorator(func):

        @wraps(func)
        async def wrapper(*args, **kwargs):
            request = kwargs.get("request")

            email = request.state.user.get("email", None)
            body = AuthRequest(email = email, password = "dummy")

            admin = auth_repository.is_admin(body)

            if not admin:
                raise UnAuthorizedException()
            
            return await func(*args, **kwargs)
        return wrapper
    return decorator


def requires_employee_role():
    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            request = kwargs.get("request")

            email = request.state.user.get("email", None)
            body = EmployeeLoginRequest(email = email, password = "dummy")

            employee = auth_repository.is_employee(body)
            if not employee:
                raise UnAuthorizedException()
            
            return await func(*args, **kwargs)
        return wrapper

    return decorator
        



