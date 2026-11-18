"""Abstract contract for employee repositories."""

from abc import ABC, abstractmethod

from employee_management.models import Employee


class EmployeeRepositoryInterface(ABC):
    """Storage operations required by the employee service."""

    @abstractmethod
    def add(self, employee: Employee) -> None:
        """Store a new employee."""

    @abstractmethod
    def get_by_id(self, employee_id: str) -> Employee | None:
        """Return an employee by ID, or None when it does not exist."""

    @abstractmethod
    def get_all(self) -> list[Employee]:
        """Return all employees."""

    @abstractmethod
    def update(self, employee: Employee) -> bool:
        """Replace an existing employee and report whether it existed."""

    @abstractmethod
    def delete(self, employee_id: str) -> bool:
        """Delete an employee and report whether it existed."""

    @abstractmethod
    def search_by_department(self, department: str) -> list[Employee]:
        """Return employees matching a department."""
