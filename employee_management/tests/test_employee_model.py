"""Tests for Employee validation and encapsulation."""

import pytest

from employee_management.errors import EmployeeValidationError
from employee_management.models import Employee


def test_create_employee_successfully() -> None:
    employee = Employee(
        "E001", " Ada Lovelace ", "ada@example.com", "Engineering", 75000
    )

    assert employee.employee_id == "E001"
    assert employee.name == "Ada Lovelace"
    assert employee.email == "ada@example.com"
    assert employee.department == "Engineering"
    assert employee.salary == 75000.0


@pytest.mark.parametrize("name", ["", "  "])
def test_validate_employee_name(name: str) -> None:
    with pytest.raises(EmployeeValidationError, match="Employee name"):
        Employee("E001", name, "ada@example.com", "Engineering", 75000)


@pytest.mark.parametrize("email", ["invalid", "a@b", "a b@example.com"])
def test_validate_email(email: str) -> None:
    with pytest.raises(EmployeeValidationError, match="Email"):
        Employee("E001", "Ada", email, "Engineering", 75000)


@pytest.mark.parametrize("salary", [-1, float("nan"), float("inf")])
def test_validate_salary(salary: float) -> None:
    with pytest.raises(EmployeeValidationError, match="Salary"):
        Employee("E001", "Ada", "ada@example.com", "Engineering", salary)


def test_employee_properties_validate_updates() -> None:
    employee = Employee("E001", "Ada", "ada@example.com", "Engineering", 75000)

    with pytest.raises(EmployeeValidationError):
        employee.name = " "

    assert employee.name == "Ada"
