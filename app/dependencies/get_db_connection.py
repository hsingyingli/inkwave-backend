
from typing import AsyncGenerator

from asyncpg.connection import asyncpg
from config.initialzers.database import db


async def get_db_conn() -> AsyncGenerator[asyncpg.Connection, None]:
    async for conn in db.get_connection():
        yield conn
