import cruds.item as crud
from database import get_db
from fastapi import APIRouter, Depends
from schemas.item import \
    Item as ItemSchema
    # Item as ItemSchema, ItemDetail as ItemDetailSchema
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

router = APIRouter()


@router.get('/', response_model=List[ItemSchema])
async def read_items(db: Session = Depends(get_db)):
    return crud.read_items(db=db)

@router.post('/', response_model=ItemSchema)
async def create_item(item: ItemSchema, db: Session = Depends(get_db)):
    return crud.create_item(item=item, db=db)

# @router.get('/{item_id}', response_model=ItemDetailSchema)
# async def read_item(item_id: UUID, db: Session = Depends(get_db)):
#     return crud.read_item(item_id=item_id, db=db)

