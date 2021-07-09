from fastapi import HTTPException
from models import User
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND
from uuid import UUID
# from schemas.user import User, UserDetail
from schemas.user import UserCreate, User as UserBase

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

def create_user(db: Session, user: UserBase):
    db_user = User(username=user.username)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
    # db_user = read_user(db, user_id=user.uuid)
    # if db_user:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    # return create_user(db=db, user=user)
