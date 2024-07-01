from ..controllers.dtos.employee_controller_dto import CreateEmployeeDTO
from ...db.repositories.employee_repository import EmployeeRepository


class EmployeeService:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository
        pass

    def create_employee(self, _employee: CreateEmployeeDTO):
        res = self.employee_repository.save(_employee)
        return res

    def get_all_employees(self):
        res = self.employee_repository.get_all_employees()
        return res
