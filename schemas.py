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






