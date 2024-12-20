from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from services import user as UserService
from dto import user as UserDTO

router = APIRouter()


@router.post('/', tags=["user"])
async def create(data: UserDTO.User = None, db: Session = Depends(get_db)):
    print(0)
    return UserService.create_user(data, db)


@router.get('/0', tags=["user"])
async def get(db: Session = Depends(get_db)):
    return UserService.list_user(db)


@router.get('/{id}', tags=["user"])
async def get(id: str = None, db: Session = Depends(get_db)):
    return UserService.get_user(id, db)


@router.put('/{id}', tags=["user"])
async def update(id: str = None, data: UserDTO.User = None, db: Session = Depends(get_db)):
    return UserService.update_user(data, db, id)


@router.delete('/{id}', tags=["user"])
async def delete(id: int = None, db: Session = Depends(get_db)):
    return UserService.delete_user(db, id)
