from typing import Any, List

from fastapi import Depends, FastAPI, HTTPException
from pydantic import UUID4
from sqlalchemy.orm import Session
from starlette.status import HTTP_201_CREATED, HTTP_404_NOT_FOUND

from app import actions, models, schemas
from app.db import SessionLocal, engine

# Create all tables in the database.
# Comment this out if you using migrations.
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session.
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/')
def index():
    return {'message': 'Hello World'}


@app.get('/user', response_model=List[schemas.User], tags=['user'])
def list_user(db: Session = Depends(get_db), skip: int=0, limit: int=100):
    users = actions.post_user.get_all(db=db, skip=skip, limit=limit)
    return users

@app.get('/company', response_model=List[schemas.Company], tags=['company']))
def list_company(db: Session = Depends(get_db), skip: int=0, limit: int=100):
    pass


























