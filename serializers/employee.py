from pydantic import BaseModel
from storage_services.types import EmployeeSkillLevel

class Skills(BaseModel):
    name: str
    skill_level: EmployeeSkillLevel