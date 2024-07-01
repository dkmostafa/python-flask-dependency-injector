from pydantic import BaseModel


class CreateEmployeeDTO(BaseModel):
    name: str
    username: str
    email: str

    class Config:
        orm_mode = True
