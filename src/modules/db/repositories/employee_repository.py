from contextlib import AbstractContextManager
from typing import Callable

from sqlalchemy.orm import Session
from ...employee.controllers.dtos.employee_controller_dto import CreateEmployeeDTO

from ..models.employee_model import EmployeeModel


class EmployeeRepository:

    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory
        pass

    def get_all_employees(self):
        with self.session_factory() as session:
            get_all_employees_res = session.query(EmployeeModel).all()
            return get_all_employees_res

    def save(self, employee: CreateEmployeeDTO):
        with self.session_factory() as session:
            new_employee = EmployeeModel(
                username=employee.username,
                email=employee.email,
                name=employee.name
            )
            session.add(new_employee)
            session.commit()
            return employee
