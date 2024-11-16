from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from config.lifespan import lifespan
from config.application import get_settings
from app.routes.router import router

settings = get_settings()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors.origins,
    allow_credentials=True,
    allow_methods=settings.cors.allow_methods,
    allow_headers=settings.cors.allow_headers,
)

app.include_router(router, prefix="/api")
app.add_exception_handler(Exception, lambda _request, _exc: JSONResponse(status_code=500, content={"message": "server error"}))

