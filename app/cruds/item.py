from fastapi import HTTPException
from models import Item
from sqlalchemy.orm import Session
from starlette.status import HTTP_404_NOT_FOUND
from uuid import UUID
# from schemas.user import User, UserDetail
from schemas.user import User as UserBase
from schemas.item import Item as ItemBase

def read_items(db: Session):
    items = db.query(Item).all()
    return items


def read_item(db: Session, item_id: UUID):
    try:
        item = db.query(Item).get(item_id)
    except BaseException:
        raise HTTPException(status_code=HTTP_404_NOT_FOUND,
                            detail='Record not found.')

    return item

def create_item(db: Session, item: ItemBase):
    db_item = Item(title=item.title)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
    # db_user = read_user(db, user_id=user.uuid)
    # if db_user:
    #     raise HTTPException(status_code=400, detail="Email already registered")
    # return create_user(db=db, user=user)

# def create_user_item(db: Session, item: )
