from ..services.employee_service import EmployeeService
from .dtos.employee_controller_dto import CreateEmployeeDTO
from flask import jsonify


class EmployeeController:

    def __init__(self, employee_service: EmployeeService):
        self.employee_service = employee_service
        pass;

    def get_all_employees(self):
        employees = self.employee_service.get_all_employees()
        return jsonify(employees)

    def create_employee(self, new_employee: CreateEmployeeDTO):
        return self.employee_service.create_employee(new_employee)
