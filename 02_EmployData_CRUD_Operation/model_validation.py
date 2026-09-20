from pydantic import BaseModel, Field;
from typing import Optional;


#Note=>  ... These Tripple Doots for the manidatari eg=> Id is maindateri, gt = GraterTher, lt= LessThen
#Note=>  Field is used to give these Parimeter in the ID, Name, Department, Age, etc.


class Employee(BaseModel):
    id: int = Field(..., gt=0)
    name: str = Field(..., min_length=3, max_length= 50, pattern= r'^[A-Za-z ]+$')
    department: str = Field(..., min_length=3, max_length= 50, pattern= r'^[A-Za-z ]+$')
    age: Optional[int] = Field(default= None)


