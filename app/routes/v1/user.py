from asyncpg import UniqueViolationError
from fastapi import Depends, status
from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from pydantic import BaseModel, EmailStr, Field
from starlette.status import HTTP_409_CONFLICT, HTTP_500_INTERNAL_SERVER_ERROR
from app.dependencies.get_db_connection import get_db_conn
from app.registories.users import CreateUserParams, create_user
from app.utils.hash import get_password_hash

user_router = APIRouter()

class CreateUserRequest(BaseModel):
    username: str = Field(pattern=r"^[0-9a-zA-Z]{1,18}$")
    email: EmailStr
    password: str = Field(pattern=r"^[0-9a-zA-Z]{8,12}$")

@user_router.post("", status_code=status.HTTP_201_CREATED)
async def create_user_route(params: CreateUserRequest, db = Depends(get_db_conn)):
    hashed_password = get_password_hash(params.password)
    result = await create_user(db, CreateUserParams(username=params.username, email=params.email, password=hashed_password)) 

    if result.is_failed and type(result.errors) == UniqueViolationError:
        return JSONResponse(status_code=HTTP_409_CONFLICT, content={"message": "duplicate fields"})
    if result.is_failed:
        return JSONResponse(status_code=HTTP_500_INTERNAL_SERVER_ERROR, content={"message": "try later"})
