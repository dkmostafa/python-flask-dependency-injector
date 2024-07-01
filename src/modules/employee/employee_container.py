import os
from dependency_injector import containers, providers

from ..db.database import Database

from .controllers.employee_controller import EmployeeController

from .services.employee_service import EmployeeService

from ..db.repositories.employee_repository import EmployeeRepository


# Repositories
class EmployeeRepositories(containers.DeclarativeContainer):
    db_url = "sqlite:///employees.db"
    db = providers.Singleton(Database, db_url=db_url)

    db_session = db.provided.session

    employee_repository = providers.Factory(EmployeeRepository, session_factory=db_session)


# Services
class EmployeeServices(containers.DeclarativeContainer):
    employee_service = providers.Factory(EmployeeService, employee_repository=EmployeeRepositories.employee_repository)


# Controllers
class EmployeeControllers(containers.DeclarativeContainer):
    employee_controller = providers.Factory(EmployeeController, employee_service=EmployeeServices.employee_service)


# Whole app container
class EmployeeContainer(containers.DeclarativeContainer):
    repositories = providers.Container(EmployeeRepositories)
    services = providers.Container(EmployeeServices)
    controllers = providers.Container(EmployeeControllers)

    # db_url = os.getenv('SQLALCHEMY_DATABASE_URI')
    # db = providers.Singleton(Database, db_url=db_url)
    # db_session = db.provided.session
