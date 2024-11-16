from contextlib import asynccontextmanager

from fastapi import FastAPI
from config.initialzers.database import db
from config.application import get_settings


settings = get_settings()

# configure life span
@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app start
    await db.connect()
    app.state.db = db
    yield
    # after app end
    await db.disconnect()
