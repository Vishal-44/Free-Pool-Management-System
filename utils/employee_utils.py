from storage_services.db_models import Employee
from serializers.admin import EmployeeSearchResult


def to_employee_search_result(employee: Employee) -> EmployeeSearchResult:
    return EmployeeSearchResult(
        id=employee.id,
        name=employee.name,
        email=employee.email,
        designation=employee.current_designation.name if employee.current_designation else None,
        department=employee.current_department.name if employee.current_department else None,
    )
