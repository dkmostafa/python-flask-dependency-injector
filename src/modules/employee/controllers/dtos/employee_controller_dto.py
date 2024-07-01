from pydantic import BaseModel


class CreateEmployeeDTO(BaseModel):
    name: str
    username: str
    email: str
