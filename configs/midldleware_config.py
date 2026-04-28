from authentication_services.jwt_authentication_service import JWTAuthenticationService


authenticaion_registry = {
    "jwt": JWTAuthenticationService()
}