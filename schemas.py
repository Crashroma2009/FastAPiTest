from typing import Optional

from pydantic import BaseModel, UUID4


class User(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = 20
    sity: Optional[str] = None


class Company(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    user_id: int


class UserCreate(User):
    first_name: str
    last_name: str
    age: int
    sity: str


class CompanyCreate(Company):
    name: str
    department: str
    user_id: int


class UserUpdate(User):
    pass


class CompanyUpdate(Company):
    pass


class UserInDB(User):
    pass


class Company(Company):
    pass
