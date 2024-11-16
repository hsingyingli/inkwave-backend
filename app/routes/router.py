from app.routes.v1.user import user_router
from fastapi.routing import APIRouter



router = APIRouter()


router.include_router(user_router, prefix="/users")



