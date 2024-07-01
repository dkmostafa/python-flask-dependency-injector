from flask_pydantic import validate
from flask import Blueprint, jsonify
from dependency_injector.wiring import Provide

from .controllers.employee_controller import EmployeeController
from .employee_container import EmployeeContainer
from .controllers.dtos.employee_controller_dto import CreateEmployeeDTO

employee_blueprint = Blueprint('employee_blueprint', __name__, url_prefix="/employee")

employee_controller: EmployeeController = Provide[EmployeeContainer.controllers.employee_controller]


@employee_blueprint.route("/", methods=["GET"])
def get_employee():
    return employee_controller.get_all_employees()


@employee_blueprint.route("/", methods=["POST"])
@validate()
def create_employee(body: CreateEmployeeDTO):
    try:
        return employee_controller.create_employee(body)
    except Exception as e:
        error_message = format(e)
        response = {
            "status": "error",
            "message": error_message
        }
        status_code = 400
        return jsonify(response), status_code

