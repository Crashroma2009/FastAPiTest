from uuid import uuid4
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.db import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid4)
    first_name = Column(String)
    last_name = Column(String)
    age = Column(Integer)
    city = Column(String)


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    department = Column(String)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)