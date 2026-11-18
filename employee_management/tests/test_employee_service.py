"""Tests for employee business operations."""

import pytest

from employee_management.errors import (
    DuplicateEmployeeError,
    EmployeeNotFoundError,
)
from employee_management.models import Employee
from employee_management.repositories import EmployeeRepository
from employee_management.services import EmployeeService


@pytest.fixture
def service() -> EmployeeService:
    return EmployeeService(EmployeeRepository())


@pytest.fixture
def employee() -> Employee:
    return Employee("E001", "Ada Lovelace", "ada@example.com", "Engineering", 75000)


def test_add_employee_with_valid_data(
    service: EmployeeService, employee: Employee
) -> None:
    service.add_employee(employee)

    assert service.get_employee("E001") is employee


def test_reject_duplicate_employee(
    service: EmployeeService, employee: Employee
) -> None:
    service.add_employee(employee)

    with pytest.raises(DuplicateEmployeeError):
        service.add_employee(employee)


def test_handle_employee_not_found(service: EmployeeService) -> None:
    with pytest.raises(EmployeeNotFoundError):
        service.get_employee("missing")

    with pytest.raises(EmployeeNotFoundError):
        service.delete_employee("missing")


def test_update_employee_information(
    service: EmployeeService, employee: Employee
) -> None:
    service.add_employee(employee)
    updated = Employee("E001", "Ada Byron", "ada@example.com", "Research", 80000)
    service.update_employee(updated)

    assert service.get_employee("E001") is updated


def test_delete_employee(
    service: EmployeeService, employee: Employee
) -> None:
    service.add_employee(employee)
    service.delete_employee("E001")

    assert service.get_all_employees() == []


def test_search_employees_by_department(
    service: EmployeeService, employee: Employee
) -> None:
    service.add_employee(employee)
    service.add_employee(
        Employee("E002", "Grace Hopper", "grace@example.com", "Naval", 82000)
    )

    assert service.search_by_department("engineering") == [employee]
