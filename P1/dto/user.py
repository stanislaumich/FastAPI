from pydantic import BaseModel


class User(BaseModel):
    name: str
    #id: int
    username: str
    password: str
    dolg: str
    dop: str
    phone: str
    email: str
    is_admin: bool
    is_active: bool
    is_superuser: bool
