from routers.auth_router import router as auth_router
from routers.admin_router import router as admin_router
from routers.employee_router import router as employee_router

routers = [auth_router, admin_router, employee_router]