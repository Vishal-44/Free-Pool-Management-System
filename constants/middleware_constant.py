import os

CONFIGURED_AUTH_SERVICE = os.getenv("AUTHENTICATION_SERVICE", "jwt").lower()
UNAUTHENTICATED_ENDPOINTS = ["/openapi.json", "/docs", "/redoc", "/token", "/auth/login", "/auth/employee/login"]