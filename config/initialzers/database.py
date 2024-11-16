from typing import AsyncGenerator
import asyncpg
import logging

from config.application import get_settings
from config.application import DatabaseSettings

logger = logging.getLogger(__name__)

class DatabaseManager:
    def __init__(self, settings: DatabaseSettings):
        self.pool: asyncpg.Pool | None = None
        self.settings: DatabaseSettings = settings 
    
    async def connect(self):
        if not self.pool:
            try:
                self.pool = await asyncpg.create_pool(
                    dsn=self.settings.dsn.__str__(),
                    min_size=self.settings.min_size,
                    max_size=self.settings.max_size,
                    command_timeout=60,
                    timeout=30
                )
            except Exception as e:
                logger.error(f"Failed to create database pool: {e}")
                raise
    
    async def disconnect(self):
        if self.pool:
            await self.pool.close()
            logger.info("Database pool closed")
    
    async def get_connection(self) -> AsyncGenerator[asyncpg.Connection, None]:
        if not self.pool:
            await self.connect()
        if self.pool:
            async with self.pool.acquire() as conn:
                yield conn 

settings = get_settings()
db = DatabaseManager(settings.database)
