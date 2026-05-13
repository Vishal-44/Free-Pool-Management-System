from pydantic import BaseModel, EmailStr

class EmployeeOnboardRequest(BaseModel):
    name: str
    email: EmailStr
    designation: str

class EmployeeOnboardResponse(BaseModel):
    email: EmailStr
    password: str

class EmployeeSearchResult(BaseModel):
    id: int
    name: str
    email: EmailStr
    designation: str | None
    department: str | None

class EmployeeSearchResponse(BaseModel):
    total: int
    page: int
    page_size: int
    items: list[EmployeeSearchResult]