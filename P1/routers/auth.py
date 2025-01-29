from fastapi import APIRouter, FastAPI, Depends, Form, Response, Cookie
from datetime import datetime
from sqlalchemy.orm import Session
from database import get_db
<<<<<<< HEAD
from services import user as UserService
from dto import user as UserDTO
from fastapi.responses import RedirectResponse, PlainTextResponse
=======
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import RedirectResponse, PlainTextResponse

from routers.static import templates

>>>>>>> d8cc68b5ef61896a297d0a76938b045e58648e88
router = APIRouter()


'''
def root():
    now = datetime.now()    # получаем текущую дату и время
    response = JSONResponse(content={"message": "куки установлены"})
    response.set_cookie(key="last_visit", value=now)
    return  response

@app.get("/")
def root(last_visit: str | None = Cookie(default=None)):
    if last_visit == None:
        return {"message": "Это ваш первый визит на сайт"}
    else:
        return  {"message": f"Ваш последний визит: {last_visit}"}    
    
'''
<<<<<<< HEAD

@router.get("/")
def postdata(response: Response, username: str | None = Cookie(default=None)):
    now = datetime.now()  # получаем текущую дату и время
    if username == None:
        return RedirectResponse("/")
    else:
        response.set_cookie(key="last_visit", value=now)

=======

@router.get("/")
def postdata(response: Response, username: str | None = Cookie(default=None)):
    now = datetime.now()  # получаем текущую дату и время
    if username == None:
        return RedirectResponse("/")
    else:
        response.set_cookie(key="last_visit", value=now)
        #return templates.TemplateResponse("/base/index.html", {"request": request})
>>>>>>> d8cc68b5ef61896a297d0a76938b045e58648e88
        return {"message": f"{username}"}


@router.post("/login")
<<<<<<< HEAD
def postdata(response: Response, username=Form(), password=Form()):
    now = datetime.now()  # получаем текущую дату и время
    response.set_cookie(key="last_visit", value=now)
    response.set_cookie(key="username", value=username, max_age=60*60*24*365)
    return {"username": username, "password": password}
=======
def postdata(response: Response, request: Request, username=Form(), password=Form()):
    now = datetime.now()  # получаем текущую дату и время
    response.set_cookie(key="last_visit", value=now)
    response.set_cookie(key="username", value=username, max_age=60*60*24*365)
    #return {"username": username, "password": password}
    return templates.TemplateResponse("/base/index.html", {"request": request})
>>>>>>> d8cc68b5ef61896a297d0a76938b045e58648e88

@router.post("/register")
def postdata(username = Form(), userage=Form()):

    return {"name": username, "age": userage}

@router.post("/unlogin")
def postdata(username = Form(), userage=Form()):
    return {"name": username, "age": userage}