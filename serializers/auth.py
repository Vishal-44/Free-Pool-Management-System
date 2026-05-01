from pydantic import BaseModel
from typing import Optional

class AuthRequest(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: str

class EmployeeLoginRequest(BaseModel):
    email: str
    password: str
