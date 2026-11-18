"""Tests for controller input handling and coordination."""

from unittest.mock import MagicMock

import pytest

from employee_management.controllers import EmployeeController
from employee_management.models import Employee
from employee_management.repositories import EmployeeRepository
from employee_management.services import EmployeeService
from employee_management.views import EmployeeView


@pytest.fixture
def view() -> MagicMock:
    return MagicMock(spec=EmployeeView)


@pytest.fixture
def service() -> EmployeeService:
    return EmployeeService(EmployeeRepository())


@pytest.fixture
def controller(
    service: EmployeeService, view: MagicMock
) -> EmployeeController:
    return EmployeeController(service, view)


def test_invalid_menu_input_is_reported(
    controller: EmployeeController, view: MagicMock
) -> None:
    assert controller.handle_choice("not-an-option") is True

    view.show_error.assert_called_once_with("Invalid menu option.")


def test_employee_creation_from_user_input(
    controller: EmployeeController,
    service: EmployeeService,
    view: MagicMock,
) -> None:
    view.get_input.side_effect = [
        "E001",
        "Ada Lovelace",
        "ada@example.com",
        "Engineering",
        "75000",
    ]

    assert controller.handle_choice("1") is True
    assert service.get_employee("E001").name == "Ada Lovelace"
    view.show_message.assert_called_once_with("Employee added successfully.")


def test_employee_listing_is_sent_to_the_view(
    controller: EmployeeController,
    service: EmployeeService,
    view: MagicMock,
) -> None:
    employee = Employee("E001", "Ada", "ada@example.com", "Engineering", 75000)
    service.add_employee(employee)

    controller.handle_choice("2")

    view.display_employees.assert_called_once_with([employee])


def test_invalid_employee_input_is_reported(
    controller: EmployeeController, view: MagicMock
) -> None:
    view.get_input.side_effect = [
        "E001",
        "",
        "ada@example.com",
        "Engineering",
        "75000",
    ]

    controller.handle_choice("1")

    view.show_error.assert_called_once()
    assert "Employee name" in view.show_error.call_args.args[0]


def test_non_numeric_salary_is_reported(
    controller: EmployeeController, view: MagicMock
) -> None:
    view.get_input.side_effect = [
        "E001",
        "Ada",
        "ada@example.com",
        "Engineering",
        "not-a-number",
    ]

    controller.handle_choice("1")

    view.show_error.assert_called_once()


def test_exit_choice_stops_the_menu(
    controller: EmployeeController, view: MagicMock
) -> None:
    assert controller.handle_choice("0") is False

    view.show_message.assert_called_once_with("Goodbye.")
