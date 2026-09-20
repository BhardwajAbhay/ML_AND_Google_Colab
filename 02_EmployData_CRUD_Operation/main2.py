from fastapi import FastAPI, HTTPException;
from model import Employee;
from typing import List;

employees_db: list[Employee] = []

app = FastAPI()

# 1) Read All Employee

@app.get('/employees', response_model=list[Employee])
def get_employees():
    return employees_db


# 2) Read Specific Employee

@app.get("/employees/{emp_id}",response_model=Employee)
def get_employee(emp_id: int):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            return employees_db[index]
    raise HTTPException(status_code=404, detail="Employee Not Found!")

# 3) Add New Employee

@app.post("/employees", response_model=Employee)
def add_employee(new_emp: Employee):
    for employee in employees_db:
        if employee.id == new_emp.id:
            raise HTTPException(status_code=400, detail="Employee Already Exists")
    employees_db.append(new_emp)
    return new_emp

# 4) Update The Employee

@app.put('/update_employee/{emp_id}', response_model=Employee)
def update_employee(emp_id: int, updated_employee: Employee):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            employees_db[index] = updated_employee
            return updated_employee
    raise HTTPException(status_code=404, detail="Employee Not Found!")


# 5) Delete Employee

@app.delete('/delete_employee/{emp_id}',response_model= Employee)
def delete_employee(emp_id: int):
    for index, employee in enumerate(employees_db):
        if employee.id == emp_id:
            del employees_db[index]
            return {'message': 'Employee Delete Successfully'}
    raise HTTPException(status_code=404, detail='Employee Not Found!')