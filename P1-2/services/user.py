from models.user import User
from sqlalchemy.orm import Session
from dto import user


def create_user(data: user.User, db: Session):
    user = User(name=data.name, username=data.username, password = data.password, dolg=data.dolg)
    print(1)
    try:
        print(2)
        db.add(user)
        print(3)
        db.commit()
        print(4)
        db.refresh(user)
        print(5)
    except Exception as e:
        print(e)

    return user


def get_user(id: int, db):
    user = db.query(User).filter(User.id == id).first()
    return user

def list_user(db):
    user = db.query(User).all()
    return user

def update_user(data: user.User, db: Session, id: int):
    user = db.query(User).filter(User.id == id).first()
    user.name = data.name
    user.email = data.email
    user.username = data.username
    user.password = data.password
    user.dolg = data.dolg
    user.dop = data.dop
    user.phone = data.phone
    user.email = data.email

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


def delete_user(db: Session, id: int):
    user = db.query(User).filter(User.id == id).delete()
    db.commit()
    return user
