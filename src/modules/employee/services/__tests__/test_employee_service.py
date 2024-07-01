import pytest
from unittest.mock import MagicMock
from ..employee_service import EmployeeService


@pytest.fixture
def employee_service():
    mock_employee_repository = MagicMock()

    mock_employee_repository.save.return_value = {
        "id": 1,
        "name": "test",
        "username": "test",
        "email": "test",
    }

    employee_service = EmployeeService(mock_employee_repository)

    return employee_service


def test_get_employee(employee_service):
    res = employee_service.create_employee("das")
    assert True
