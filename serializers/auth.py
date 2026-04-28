from pydantic import BaseModel, field_validator
from typing import Optional

class AuthRequest(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: str
