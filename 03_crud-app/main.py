import models, schemas, crud;
from fastapi import FastAPI, HTTPException, Depends;
from sqlalchemy.orm import session;
from database import engine, SessionLocal, Base;
from typing import List;

Base.metadata.create_all(bind=engine)

app = FastAPI()

# dependency with the DB

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# EndPoint

# 1) create an employee

@app.post('/emplouees', response_model= schemas.EmployeeOut)
def create_employee(employee: schemas.EmployeeCreate, db: session = Depends(get_db)):
    return crud.create_employee(db, employee)

# 2) get all employees

@app.get('/employees', response_model= List[schemas.EmployeeOut])
def get_employees(db: session = Depends(get_db)):
    return crud.get_employee(db)

# 3) get specific employee

@app.get('/employee/{emp_id}', response_model= schemas.EmployeeOut)
def get_employee(emp_id: int, db: session = Depends(get_db)):
    employee = crud.get_employee(db, emp_id)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found!')
    return employee

# 4) update employee

@app.put('/employee/{emp_id}', response_model= schemas.EmployeeOut)
def update_employee(emp_id: int, employee: schemas.update_employee, db: session = Depends(get_db)):
    db_employee = crud.update_employee(db,employee, emp_id)
    if db_employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found!')
    return db_employee

# 5) delete employee

@app.delete('/employee/{emp_id}', response_model= schemas.EmployeeOut)
def delete_employee(emp_id: int, db: session = Depends(get_db)):
    employee = crud.delete_employee(emp_id, db)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found!')
    return employee

# 5) delete employee

@app.delete('/employee/{emp_id}', response_model= dict)
def delete_employee(emp_id: int, db: session = Depends(get_db)):
    employee = crud.delete_employee(emp_id, db)
    if employee is None:
        raise HTTPException(status_code=404, detail='Employee Not Found!')
    return {'detail': 'Employee Deleted'}