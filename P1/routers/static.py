from fastapi import APIRouter, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from sqlalchemy.orm import Session
from database import get_db
from services import user as UserService

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get('/', tags=["static"], response_class=HTMLResponse)
async def get(request: Request):


    return templates.TemplateResponse("/base/login.html", {"request": request})