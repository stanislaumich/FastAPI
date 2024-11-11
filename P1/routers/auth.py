from fastapi import APIRouter, FastAPI, Depends, Form, Response, Cookie
from datetime import datetime
from sqlalchemy.orm import Session
from database import get_db
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import RedirectResponse, PlainTextResponse

from routers.static import templates

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

@router.get("/")
def postdata(response: Response, username: str | None = Cookie(default=None)):
    now = datetime.now()  # получаем текущую дату и время
    if username == None:
        return RedirectResponse("/")
    else:
        response.set_cookie(key="last_visit", value=now)
        #return templates.TemplateResponse("/base/index.html", {"request": request})
        return {"message": f"{username}"}


@router.post("/login")
def postdata(response: Response, request: Request, username=Form(), password=Form()):
    now = datetime.now()  # получаем текущую дату и время
    response.set_cookie(key="last_visit", value=now)
    response.set_cookie(key="username", value=username, max_age=60*60*24*365)
    #return {"username": username, "password": password}
    return templates.TemplateResponse("/base/index.html", {"request": request})

@router.post("/register")
def postdata(username = Form(), userage=Form()):

    return {"name": username, "age": userage}

@router.post("/unlogin")
def postdata(username = Form(), userage=Form()):
    return {"name": username, "age": userage}