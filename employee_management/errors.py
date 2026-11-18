"""Domain exceptions used by the employee management system."""


class EmployeeManagementError(Exception):
    """Base exception for expected employee management errors."""


class EmployeeValidationError(EmployeeManagementError, ValueError):
    """Raised when an employee field contains invalid data."""


class DuplicateEmployeeError(EmployeeManagementError):
    """Raised when an employee ID is already in use."""


class EmployeeNotFoundError(EmployeeManagementError):
    """Raised when an employee cannot be found."""
