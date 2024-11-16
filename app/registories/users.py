from asyncpg import Connection
from asyncpg.exceptions import UniqueViolationError
from pydantic import BaseModel, EmailStr, Field

from app.utils.monadic import async_monadic

class CreateUserParams(BaseModel):
    username: str = Field(pattern=r"^[0-9a-zA-Z]{1,18}$")
    email: EmailStr
    password: str 


create_user_query = '''
    INSERT INTO users(username, email, password)
    VALUES ($1, $2, $3)
'''

@async_monadic
async def create_user(conn: Connection, create_user_params: CreateUserParams):
    await conn.execute(create_user_query, create_user_params.username, create_user_params.email, create_user_params.password)
