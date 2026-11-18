"""In-memory employee repository."""

from employee_management.errors import DuplicateEmployeeError
from employee_management.interfaces import EmployeeRepositoryInterface
from employee_management.models import Employee


class EmployeeRepository(EmployeeRepositoryInterface):
    """Dictionary-backed repository implementing the storage contract."""

    def __init__(self) -> None:
        self._employees: dict[str, Employee] = {}

    def add(self, employee: Employee) -> None:
        if employee.employee_id in self._employees:
            raise DuplicateEmployeeError(
                f"Employee ID '{employee.employee_id}' already exists."
            )
        self._employees[employee.employee_id] = employee

    def get_by_id(self, employee_id: str) -> Employee | None:
        return self._employees.get(employee_id)

    def get_all(self) -> list[Employee]:
        return list(self._employees.values())

    def update(self, employee: Employee) -> bool:
        if employee.employee_id not in self._employees:
            return False
        self._employees[employee.employee_id] = employee
        return True

    def delete(self, employee_id: str) -> bool:
        return self._employees.pop(employee_id, None) is not None

    def search_by_department(self, department: str) -> list[Employee]:
        normalized_department = department.strip().casefold()
        return [
            employee
            for employee in self._employees.values()
            if employee.department.casefold() == normalized_department
        ]
