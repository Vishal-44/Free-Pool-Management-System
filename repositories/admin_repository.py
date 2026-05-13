from datetime import datetime
from sqlalchemy import or_

from storage_services.database_service import DatabaseService
from storage_services.db_models import (
    Certification, Designation, DesignationRecord, Employee,
    EmployeeCertificationMap, EmployeeSkillMap, Skill,
)
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

            # Trigger lazy-load of the designation chain while session is open.
            # current_designation / current_department are properties on Employee
            # that filter designation_records to the active record (end_date is None).
            for emp in employees:
                _ = emp.current_designation
                _ = emp.current_department

            return total, employees

