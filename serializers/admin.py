from pydantic import BaseModel, EmailStr

class EmployeeOnboardRequest(BaseModel):
    name: str
    email: EmailStr
    designation: str
    
class EmployeeOnboardResponse(BaseModel):
    email: EmailStr
    password: str