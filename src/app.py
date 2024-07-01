from flask import Flask
from src.modules.employee import employee_routes
from src.modules.employee.employee_container import EmployeeContainer

app = Flask(__name__)

app.register_blueprint(employee_routes.employee_blueprint)

employee_container = EmployeeContainer()

employee_container.wire(
    modules=[employee_routes.__name__]
)

if __name__ == "__main__":
    app.run(debug=True)
