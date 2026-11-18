"""Console presentation for employee operations."""

from collections.abc import Sequence

from employee_management.models import Employee


class EmployeeView:
    """Read console input and display application output."""

    def display_menu(self) -> None:
        print(
            "\nEmployee Management System\n"
            "1. Add employee\n"
            "2. View all employees\n"
            "3. Get employee by ID\n"
            "4. Update employee\n"
            "5. Delete employee\n"
            "6. Search by department\n"
            "0. Exit"
        )

    def get_input(self, prompt: str) -> str:
        """Prompt for and return a line of user input."""
        return input(prompt).strip()

    def display_employees(self, employees: Sequence[Employee]) -> None:
        """Display a collection of employee records."""
        if not employees:
            print("No employees found.")
            return

        print(
            f"{'ID':<12} {'Name':<22} {'Email':<32} "
            f"{'Department':<18} {'Salary':>12}"
        )
        print("-" * 100)
        for employee in employees:
            print(
                f"{employee.employee_id:<12} {employee.name:<22} "
                f"{employee.email:<32} {employee.department:<18} "
                f"{employee.salary:>12,.2f}"
            )

    def display_employee(self, employee: Employee) -> None:
        """Display one employee record."""
        self.display_employees([employee])

    def show_message(self, message: str) -> None:
        """Display an informational message."""
        print(message)

    def show_error(self, message: str) -> None:
        """Display an error message."""
        print(f"Error: {message}")
