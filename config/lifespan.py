from contextlib import asynccontextmanager

from fastapi import FastAPI

# configure life span
@asynccontextmanager
async def lifespan(app: FastAPI):
    # before app start
    yield
    # after app end
