from datetime import datetime

from storage_services.database_service import DatabaseService
from storage_services.db_models import Designation, DesignationRecord, Employee
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
            session.refresh(employee)
            return employee
    
    def get_designation_by_name(self, name: str) -> Designation | None:
        with self.get_session() as session:
            return session.query(Designation).filter(Designation.name == name).first()

