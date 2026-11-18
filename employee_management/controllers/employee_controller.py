"""Coordinate console input, application services, and view output."""

from employee_management.errors import EmployeeManagementError
from employee_management.models import Employee
from employee_management.services import EmployeeService
from employee_management.views import EmployeeView


class EmployeeController:
    """Handle menu choices while leaving business rules to the service."""

    def __init__(self, service: EmployeeService, view: EmployeeView) -> None:
        self._service = service
        self._view = view

    def run(self) -> None:
        """Run the interactive menu until the user chooses to exit."""
        while True:
            self._view.display_menu()
            if not self.handle_choice(self._view.get_input("Choose an option: ")):
                break

    def handle_choice(self, choice: str) -> bool:
        """Process one menu choice; return False when the user exits."""
        actions = {
            "1": self._add_employee,
            "2": self._list_employees,
            "3": self._get_employee,
            "4": self._update_employee,
            "5": self._delete_employee,
            "6": self._search_employees,
        }

        if choice == "0":
            self._view.show_message("Goodbye.")
            return False

        action = actions.get(choice)
        if action is None:
            self._view.show_error("Invalid menu option.")
            return True

        try:
            action()
        except (EmployeeManagementError, ValueError) as error:
            self._view.show_error(str(error))
        return True

    def _read_employee(self, employee_id: str | None = None) -> Employee:
        if employee_id is None:
            employee_id = self._view.get_input("Employee ID: ")
        name = self._view.get_input("Name: ")
        email = self._view.get_input("Email: ")
        department = self._view.get_input("Department: ")
        salary = float(self._view.get_input("Salary: "))
        return Employee(employee_id, name, email, department, salary)

    def _add_employee(self) -> None:
        employee = self._read_employee()
        self._service.add_employee(employee)
        self._view.show_message("Employee added successfully.")

    def _list_employees(self) -> None:
        self._view.display_employees(self._service.get_all_employees())

    def _get_employee(self) -> None:
        employee_id = self._view.get_input("Employee ID: ")
        self._view.display_employee(self._service.get_employee(employee_id))

    def _update_employee(self) -> None:
        employee_id = self._view.get_input("Employee ID to update: ")
        self._service.get_employee(employee_id)
        updated_employee = self._read_employee(employee_id)
        self._service.update_employee(updated_employee)
        self._view.show_message("Employee updated successfully.")

    def _delete_employee(self) -> None:
        employee_id = self._view.get_input("Employee ID to delete: ")
        self._service.delete_employee(employee_id)
        self._view.show_message("Employee deleted successfully.")

    def _search_employees(self) -> None:
        department = self._view.get_input("Department: ")
        self._view.display_employees(
            self._service.search_by_department(department)
        )
