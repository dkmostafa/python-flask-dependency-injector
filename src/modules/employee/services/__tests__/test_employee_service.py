import pytest
from unittest.mock import MagicMock
from ..employee_service import EmployeeService
from ...controllers.dtos.employee_controller_dto import CreateEmployeeDTO


@pytest.fixture
def employee_service():
    mock_employee_repository = MagicMock()

    mock_employee_repository.save.return_value = {
        "id": 1,
        "name": "test",
        "username": "test",
        "email": "test",
    }
    mock_employee_repository.get_all_employees.return_value = [
        {
            "email": "test",
            "id": 1,
            "name": "test",
            "username": "test"
        }
    ]

    employee_service = EmployeeService(mock_employee_repository)

    return employee_service


def test_create_employee(employee_service):
    create_employee_mock_input = CreateEmployeeDTO(
        name="test",
        username="test",
        email="test",
    )
    res = employee_service.create_employee(create_employee_mock_input)

    assert res == {
        "id": 1,
        "name": "test",
        "username": "test",
        "email": "test",
    }

    assert True


def test_get_employees(employee_service):
    res = employee_service.get_all_employees()
    assert res == [
        {
            "email": "test",
            "id": 1,
            "name": "test",
            "username": "test"
        }
    ]
