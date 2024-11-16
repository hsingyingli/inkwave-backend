from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.lifespan import lifespan
from config.application import get_settings

settings = get_settings()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors.origins,
    allow_credentials=True,
    allow_methods=settings.cors.allow_methods,
    allow_headers=settings.cors.allow_headers,
)

# app.include_router(router, prefix="/api")
