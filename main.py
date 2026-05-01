from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI ,status
from fastapi.responses import JSONResponse

from authentication_services.jwt_authentication_service import JWTAuthenticationService
from middlewares.authentication_middleware import AuthenticationMiddleware
from serializers.response import APIResponse
from constants.exception_constants import INTERNAL_SERVER_ERROR_MESSAGE
from configs.app_config import routers
from exceptions import (
    BaseException,
    InvalidRequestException, 
    UnAutenticatedException, 
    NotFoundException,
    AlreadyExistsException
)
from constants.app_constants import (
    APP_NAME, 
    APP_DESCRIPTION, 
    APP_VERSION
)


app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=APP_VERSION
)


app.add_middleware(AuthenticationMiddleware)


for router in routers:
    app.include_router(
        router = router
    )


@app.get("/health")
async def health_check():
    return JSONResponse(
        status_code = status.HTTP_200_OK,
        content = APIResponse(
            message="Service is healthy"
        ).model_dump()
    )

@app.get("/token")
async def get_token():
    token = JWTAuthenticationService().create_jwt_token({"username": "testuser"})
    return JSONResponse(
        status_code = status.HTTP_200_OK,
        content = APIResponse(
            message="Token generated successfully",
            data={"token": token}
        ).model_dump()
    )

@app.exception_handler(BaseException)
async def exception_handler(request, exc: BaseException):
    return JSONResponse(
        status_code=exc.status_code,
        content=APIResponse(
            message=str(exc)
        ).model_dump()
    )

@app.exception_handler(Exception)
async def generic_exception_handler(request, exc: Exception):
    return JSONResponse(
        status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
        content = APIResponse(
            message = INTERNAL_SERVER_ERROR_MESSAGE
        ).model_dump()
    )