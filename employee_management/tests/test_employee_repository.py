"""Tests for the in-memory employee repository."""

import pytest

from employee_management.errors import DuplicateEmployeeError
from employee_management.models import Employee
from employee_management.repositories import EmployeeRepository


@pytest.fixture
def repository() -> EmployeeRepository:
    return EmployeeRepository()


@pytest.fixture
def employee() -> Employee:
    return Employee("E001", "Ada Lovelace", "ada@example.com", "Engineering", 75000)


def test_add_and_retrieve_employee(
    repository: EmployeeRepository, employee: Employee
) -> None:
    repository.add(employee)

    assert repository.get_by_id("E001") is employee


def test_retrieve_all_employees(
    repository: EmployeeRepository, employee: Employee
) -> None:
    repository.add(employee)

    assert repository.get_all() == [employee]


def test_update_employee(
    repository: EmployeeRepository, employee: Employee
) -> None:
    repository.add(employee)
    updated = Employee("E001", "Ada Byron", "ada@example.com", "Research", 80000)

    assert repository.update(updated) is True
    assert repository.get_by_id("E001") is updated


def test_delete_employee(
    repository: EmployeeRepository, employee: Employee
) -> None:
    repository.add(employee)

    assert repository.delete("E001") is True
    assert repository.get_by_id("E001") is None
    assert repository.delete("E001") is False


def test_search_by_department(
    repository: EmployeeRepository, employee: Employee
) -> None:
    repository.add(employee)
    repository.add(
        Employee("E002", "Grace Hopper", "grace@example.com", "Naval", 82000)
    )

    assert repository.search_by_department("engineering") == [employee]


def test_reject_duplicate_employee_ids(
    repository: EmployeeRepository, employee: Employee
) -> None:
    repository.add(employee)

    with pytest.raises(DuplicateEmployeeError):
        repository.add(
            Employee("E001", "Another Person", "other@example.com", "Sales", 50000)
        )


def test_missing_employee_update_returns_false(
    repository: EmployeeRepository, employee: Employee
) -> None:
    assert repository.update(employee) is False
