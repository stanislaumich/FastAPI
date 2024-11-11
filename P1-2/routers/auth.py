from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from database import get_db
from services import user as UserService
from dto import user as UserDTO

router = APIRouter()


@router.post("/login")
def postdata(username = Form(), password=Form()):

    return {"username": username, "password": password}

@router.post("/register")
def postdata(username = Form(), userage=Form()):

    return {"name": username, "age": userage}

@router.post("/unlogin")
def postdata(username = Form(), userage=Form()):
    return {"name": username, "age": userage}