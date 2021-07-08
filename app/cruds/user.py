from fastapi import HTTPException
from models import User
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND
from uuid import UUID
from schemas import User


def read_users(db: Session):
    items = db.query(User).all()
    return items


def read_user(db: Session, user_id: UUID):
    try:
        item = db.query(User).get(user_id)
    except BaseException:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')

    return item

def create_user(db: Session, user: User):
    db_user = read_user(db, user_id=user.user_id)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)
