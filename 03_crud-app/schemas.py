from pydantic import BaseModel, EmailStr;

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr


class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(EmployeeBase):
    pass

class EmployeeOut(EmployeeBase):
    id: int

    class config:
        orm_mode = True #This is for the Pass the SQLalchemy date Allows pydantic to read the date directly from the ORM object
        # enables smooth coversion to JSON