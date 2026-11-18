"""Employee business logic."""

from employee_management.errors import EmployeeNotFoundError
from employee_management.interfaces import EmployeeRepositoryInterface
from employee_management.models import Employee


class EmployeeService:
    """Apply employee business rules using an injected repository."""

    def __init__(self, repository: EmployeeRepositoryInterface) -> None:
        self._repository = repository

    def add_employee(self, employee: Employee) -> None:
        """Add an employee, rejecting duplicate IDs in the repository."""
        self._repository.add(employee)

    def get_employee(self, employee_id: str) -> Employee:
        """Return an employee or raise when the ID is unknown."""
        employee = self._repository.get_by_id(employee_id)
        if employee is None:
            raise EmployeeNotFoundError(
                f"Employee with ID '{employee_id}' was not found."
            )
        return employee

    def get_all_employees(self) -> list[Employee]:
        """Return all stored employees."""
        return self._repository.get_all()

    def update_employee(self, employee: Employee) -> None:
        """Update an existing employee."""
        self.get_employee(employee.employee_id)
        self._repository.update(employee)

    def delete_employee(self, employee_id: str) -> None:
        """Delete an existing employee."""
        if not self._repository.delete(employee_id):
            raise EmployeeNotFoundError(
                f"Employee with ID '{employee_id}' was not found."
            )

    def search_by_department(self, department: str) -> list[Employee]:
        """Find employees in the requested department."""
        return self._repository.search_by_department(department)
