from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    age: int

app = FastAPI()

@app.get("/user", response_model=User)
def get_user():
    return User(
        id=1,
        name="Abhay",
        age=12
    )


# pydantic_demo(
#     path: "/user",
#     endpoint: get_user,
#     methods = get,
#     response_model = user
# )

# from fastapi import FastAPI
# from pydantic import BaseModel

class Owner(BaseModel):
    id: int
    name: str
    city: str
    age: int

app = FastAPI()

@app.get('/owner', response_model=Owner)
def get_Owner():
    return Owner(
        id=12445,
        name='Aditya',
        city='Agra',
        age=34
    )


# path: '/owner'
# endpoint: get_Owner
# method: get
# respose_model: Owner
