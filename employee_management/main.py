"""Application composition root and entry point."""

from employee_management.controllers import EmployeeController
from employee_management.repositories import EmployeeRepository
from employee_management.services import EmployeeService
from employee_management.views import EmployeeView


def main() -> None:
    """Wire application dependencies and start the console interface."""
    repository = EmployeeRepository()
    service = EmployeeService(repository)
    view = EmployeeView()
    controller = EmployeeController(service, view)
    controller.run()


if __name__ == "__main__":
    main()
