from datetime import datetime
from sqlalchemy import func, or_
from sqlalchemy.orm import joinedload, selectinload

from storage_services.database_service import DatabaseService
from storage_services.db_models import (
    Certification, Department, Designation, DesignationRecord, Employee,
    EmployeeCertificationMap, EmployeeSkillMap, ProjectEmployeeMap, Skill,
)
from storage_services.types import EmployeeStatus
from serializers.admin import EmployeeOnboardRequest

class AdminRepository(DatabaseService):

    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(AdminRepository, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def get_employee_by_email(self, email: str) -> Employee | None:
        with self.get_session() as session:
            return session.query(Employee).filter(Employee.email == email).first()

    def create_employee(self, payload: EmployeeOnboardRequest, password: str, designation: Designation) -> Employee:
        with self.get_session() as session:
            employee = Employee(
                name=payload.name,
                email=payload.email,
                password=password,
                start_date=datetime.utcnow()
            )
            session.add(employee)
            session.flush()
            employee.designation_records.append(
                DesignationRecord(
                    employee_id=employee.id,
                    designation_id=designation.id
                )
            )
            return employee
    
    def get_designation_by_name(self, name: str) -> Designation | None:
        with self.get_session() as session:
            return session.query(Designation).filter(Designation.name == name).first()

    def search_employees(self, query: str, page: int, page_size: int) -> tuple[int, list[Employee]]:
        with self.get_session() as session:
            query = f"%{query}%"
            base = (
                session.query(Employee)
                .options(
                    selectinload(Employee.designation_records)
                        .joinedload(DesignationRecord.designation)
                        .joinedload(Designation.department),
                )
                .distinct()
                .outerjoin(Employee.skill_maps)
                .outerjoin(EmployeeSkillMap.skill)
                .outerjoin(Employee.certification_maps)
                .outerjoin(EmployeeCertificationMap.certification)
                .filter(
                    or_(
                        Employee.name.ilike(query),
                        Employee.email.ilike(query),
                        Skill.name.ilike(query),
                        Certification.name.ilike(query),
                    )
                )
            )
            total = base.count()
            employees = base.offset((page - 1) * page_size).limit(page_size).all()
            return total, employees

    def list_employees(
        self,
        status: EmployeeStatus | None,
        department: str | None,
        designation: str | None,
        skills: list[str] | None,
        page: int,
        page_size: int,
    ) -> tuple[int, list[Employee]]:
        with self.get_session() as session:
            base = session.query(Employee).options(
                selectinload(Employee.designation_records)
                    .joinedload(DesignationRecord.designation)
                    .joinedload(Designation.department),
                selectinload(Employee.project_maps)
                    .joinedload(ProjectEmployeeMap.project),
            )

            if department is not None or designation is not None:
                base = (
                    base
                    .join(Employee.designation_records)
                    .filter(DesignationRecord.end_date.is_(None))
                    .join(DesignationRecord.designation)
                )
                if designation is not None:
                    base = base.filter(func.lower(Designation.name) == designation.lower())
                if department is not None:
                    base = base.join(Designation.department).filter(
                        func.lower(Department.name) == department.lower()
                    )

            if skills:
                # AND across skills: employee must have every skill listed.
                distinct_skills = list({s.lower() for s in skills})
                skill_match_subquery = (
                    session.query(EmployeeSkillMap.employee_id)
                    .join(EmployeeSkillMap.skill)
                    .filter(func.lower(Skill.name).in_(distinct_skills))
                    .group_by(EmployeeSkillMap.employee_id)
                    .having(func.count(func.distinct(Skill.id)) == len(distinct_skills))
                )
                base = base.filter(Employee.id.in_(skill_match_subquery))

            if status is not None:
                base = base.filter(Employee.status == status)

            base = base.distinct()

            total = base.count()
            employees = (
                base.order_by(Employee.id)
                    .offset((page - 1) * page_size)
                    .limit(page_size)
                    .all()
            )
            return total, employees

    def list_skills(
        self,
        domain: str | None,
        page: int,
        page_size: int,
    ) -> tuple[int, list[Skill]]:
        with self.get_session() as session:
            base = session.query(Skill)

            if domain is not None:
                base = base.filter(func.lower(Skill.domain) == domain.lower())

            total = base.count()
            skills = (
                base.order_by(Skill.domain, Skill.name)
                    .offset((page - 1) * page_size)
                    .limit(page_size)
                    .all()
            )
            return total, skills
