from pydantic import BaseModel
from uuid import UUID


class Item(BaseModel):
    uuid: UUID
    title: str

    class Config:
        orm_mode = True


# class ItemDetail(Item):

