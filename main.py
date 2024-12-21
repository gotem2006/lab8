# for start past this code 
# "python -m uvicorn main:app --reload" 

from fastapi import FastAPI
 
app = FastAPI()

#1 Создание базового API
@app.get("/")
async def read_root():
    return {"MESSAGE": "Hello world!!!21"}
 
# 2 Обработка параметров
@app.get("/greet/{name}")
async def greet(name: str):
    return {"message":f"Hello .{name}!"}

@app.get("/search")
async def search(query: str):
    return {"message": f"You searched for: {query}"}

#3 Отправка различных типов данных
@app.get("/json")
async def JASON(name: str,age:int,hobby:str):
    return {
        "Name is ":name,
        "Your age is ": age,
        "Hibby is ": hobby
    }
from fastapi.responses import FileResponse, RedirectResponse
@app.get("/file")
async def send_file():
    return FileResponse("example.txt")

@app.get("/redirect")
async def redirect_to_root():
    return RedirectResponse("/")

#4 Работа с заголовками и куками
from fastapi import Request, Response

@app.get("/headers")
async def get_headers(request: Request):
    return dict(request.headers)

@app.get("/set-cookie")
async def set_cookie(response: Response):
    response.set_cookie(key="Welcome_To", value="Polytech")
    return {"message": "Cookie set!"}

@app.get("/get-cookie")
async def get_cookie(request: Request):
    value = request.cookies.get("Welcome_To")
    return {"Welcome_To": value}
#5. Обработка данных запроса
from fastapi import Form

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    return {"message": f"Welcome, {username}!"}

@app.post("/register")
async def register(data: dict):
    username = data.get("username")
    return {"message": f"User {username} registered successfully!"}

#6 Работа с классами 
from pydantic import BaseModel
from typing import List

class User(BaseModel):
    id: int
    username: str
    email: str
    password: str
users = [
    User(id=1, username="Вася", email="Вася@example.com", password="pass1"),
    User(id=2, username="Петя", email="Петя@example.com", password="pass2"),
]
@app.get("/users", response_model=List[User])
async def get_users():
    return users

@app.get("/users/{id}", response_model=User)
async def get_user(id: int):
    for user in users:
        if user.id == id:
            return user
    return {"error": "User not found"}