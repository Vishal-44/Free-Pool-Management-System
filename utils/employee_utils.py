from storage_services.db_models import Employee
from serializers.admin import EmployeeListItem, EmployeeSearchResult


def to_employee_search_result(employee: Employee) -> EmployeeSearchResult:
    return EmployeeSearchResult(
        id=employee.id,
        name=employee.name,
        email=employee.email,
        designation=employee.current_designation.name if employee.current_designation else None,
        department=employee.current_department.name if employee.current_department else None,
    )


def to_employee_list_item(employee: Employee) -> EmployeeListItem:
    designation_record = employee.current_designation_record
    designation = designation_record.designation if designation_record else None
    department = designation.department if designation else None

    current_project_map = next(
        (m for m in employee.project_maps if m.end_date is None),
        None,
    )

    return EmployeeListItem(
        id=employee.id,
        name=employee.name,
        email=employee.email,
        designation=designation.name if designation else None,
        department=department.name if department else None,
        status=employee.status.value,
        current_project=current_project_map.project.name if current_project_map else None,
    )
