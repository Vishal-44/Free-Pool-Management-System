from typing import List, Optional

from storage_services.database_service import DatabaseService
from serializers.employee import Skills as SkillModel
from storage_services.db_models import Employee, EmployeeSkillMap, Skill
from storage_services.types import EmployeeStatus
from exceptions import NotFoundException


class EmployeeRepository(DatabaseService):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(EmployeeRepository, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def update_employee(
        self,
        email: str,
        description: Optional[str] = None,
        skills: Optional[List[SkillModel]] = None,
        image_url: Optional[str] = None,
    ) -> Employee:
        with self.get_session() as session:
            employee = self._get_employee(email, session)

            if not employee:
                raise NotFoundException("Employee not found.")

            if description is not None:     
                employee.description = description

            if image_url is not None:       
                employee.image_url = image_url

            if skills is not None:
                self._update_skills(skills=skills, employee=employee, session=session)

            session.commit()
            session.refresh(employee)
            return employee

    def _update_skills(self, skills: List[SkillModel], employee: Employee, session) -> None:
        skill_rows = (
            session.query(Skill)
            .filter(Skill.name.in_({s.name for s in skills}))
            .all()
        )
        skill_id_map = {row.name: row.id for row in skill_rows}

        missing = {s.name for s in skills} - skill_id_map.keys()
        if missing:
            raise NotFoundException(f"Skills not found: {', '.join(missing)}")

        employee.skill_maps = [
            EmployeeSkillMap(
                employee_id=employee.id,
                skill_id=skill_id_map[s.name],
                skill_level=s.skill_level,
            )
            for s in skills
        ]

    def _get_employee(self, email: str, session) -> Optional[Employee]:  
        return (
            session.query(Employee)
            .filter(
                Employee.email == email,
                Employee.status == EmployeeStatus.WORKING,
            )
            .first()
        )