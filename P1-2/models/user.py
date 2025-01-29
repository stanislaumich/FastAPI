from sqlalchemy import Column, Integer, String, DateTime, Boolean
from database import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index = True, autoincrement=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)

    name = Column(String, unique=True, index=True, nullable=False)
    dolg = Column(String)
    dop = Column(String)
    phone = Column(String)
    email = Column(String)
    is_admin = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean, default=False)
