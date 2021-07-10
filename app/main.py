from fastapi import FastAPI, APIRouter
from routers.user import router as user_router
from routers.item import router as item_router

router = APIRouter()
router.include_router(
    user_router,
    prefix='/users',
    tags=['users']
)
router.include_router(
    item_router,
    prefix='/items',
    tags=['items']
)

app = FastAPI()
app.include_router(router)
