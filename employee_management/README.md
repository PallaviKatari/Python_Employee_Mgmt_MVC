# Employee Management System

A beginner-friendly console application demonstrating a layered, MVC-style
Python design. Employee records are stored in memory and are lost when the
application exits.

## Requirements

- Python 3.12 or newer
- pytest to run the test suite

## Run the application

From the workspace root (the directory containing `employee_management`), run:

```powershell
python -m employee_management.main
```

## Run the tests

Install pytest and run the test suite from the workspace root:

```powershell
python -m pip install pytest
python -m pytest employee_management/tests
```

## Layers

- `models`: employee data and field validation
- `interfaces`: abstract repository contract
- `repositories`: in-memory storage implementation
- `services`: employee business operations
- `controllers`: menu input handling and coordination
- `views`: console input and output
- `tests`: model, repository, service, and controller tests

The application entry point (`main.py`) wires the repository, service, view,
and controller through constructor-based dependency injection.

## Original project prompt

The project was created from this prompt:

> Act as a Senior Python Software Architect and Python Trainer. Create a
> beginner-friendly but professionally structured Python project called
> **Employee Management System** using a layered MVC-style architecture.
>
> Develop a simple employee management system with these operations: add an
> employee, view all employees, get employee details by ID, update employee
> information, delete an employee, and search employees by department.
> Employees have an ID, name, email, department, and salary. Use an in-memory
> data store; do not introduce a database or web framework.
>
> Separate concerns into a Model (employee data and validation), View
> (console UI), Controller (user input and coordination), Service (business
> logic), Interfaces (abstract contracts using Python ABC), and Repository
> (storage and retrieval). Use dependency injection where appropriate.
>
> Organize the code into `models`, `interfaces`, `repositories`, `services`,
> `controllers`, `views`, and `tests` packages, with `main.py` as the entry
> point. Each package should have an `__init__.py`. Include an employee model,
> an abstract `EmployeeRepositoryInterface` with `add`, `get_by_id`,
> `get_all`, `update`, `delete`, and `search_by_department` methods, and an
> `EmployeeRepository` implementation.
>
> Demonstrate classes and objects, encapsulation, inheritance, abstract base
> classes and methods, polymorphism, method overriding, dependency injection,
> exception handling, and type hints.
>
> Use pytest. Test model creation and validation (name, email, salary);
> repository add, retrieval, update, delete, department search, and duplicate
> IDs; service add, duplicate rejection, not-found handling, update, delete,
> and search; and controller input handling, employee creation and listing,
> and invalid input. Use pytest fixtures and `unittest.mock` where appropriate.
>
> Target Python 3.12 or newer. Keep the code clean, readable, documented, and
> PEP 8 compliant. Use custom exceptions where appropriate, avoid unnecessary
> external dependencies, and do not put all logic in one file. Keep business
> logic out of the console view.
