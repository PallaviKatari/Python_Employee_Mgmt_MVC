"""Employee model and field validation."""

import math
import re

from employee_management.errors import EmployeeValidationError


class Employee:
    """An employee record with validated, encapsulated attributes."""

    _EMAIL_PATTERN = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")

    def __init__(
        self,
        employee_id: str,
        name: str,
        email: str,
        department: str,
        salary: float,
    ) -> None:
        self._employee_id = self._validate_text(employee_id, "Employee ID")
        self.name = name
        self.email = email
        self.department = department
        self.salary = salary

    @staticmethod
    def _validate_text(value: str, field_name: str) -> str:
        if not isinstance(value, str) or not value.strip():
            raise EmployeeValidationError(f"{field_name} cannot be empty.")
        return value.strip()

    @property
    def employee_id(self) -> str:
        """Return the immutable employee identifier."""
        return self._employee_id

    @property
    def name(self) -> str:
        """Return the employee's name."""
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = self._validate_text(value, "Employee name")

    @property
    def email(self) -> str:
        """Return the employee's email address."""
        return self._email

    @email.setter
    def email(self, value: str) -> None:
        email = self._validate_text(value, "Email")
        if not self._EMAIL_PATTERN.fullmatch(email):
            raise EmployeeValidationError("Email address is not valid.")
        self._email = email

    @property
    def department(self) -> str:
        """Return the employee's department."""
        return self._department

    @department.setter
    def department(self, value: str) -> None:
        self._department = self._validate_text(value, "Department")

    @property
    def salary(self) -> float:
        """Return the employee's salary."""
        return self._salary

    @salary.setter
    def salary(self, value: float) -> None:
        if (
            isinstance(value, bool)
            or not isinstance(value, (int, float))
            or not math.isfinite(value)
            or value < 0
        ):
            raise EmployeeValidationError(
                "Salary must be a non-negative finite number."
            )
        self._salary = float(value)

    def __repr__(self) -> str:
        return (
            "Employee("
            f"employee_id={self.employee_id!r}, "
            f"name={self.name!r}, "
            f"email={self.email!r}, "
            f"department={self.department!r}, "
            f"salary={self.salary!r})"
        )
