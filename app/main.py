from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from app.middlewares.auth_middleware import CustomAuthMiddleware
from app.routers.settings_router import settings_router
from app.storage import Storage
from starlette.middleware.authentication import AuthenticationMiddleware
from starlette.requests import HTTPConnection
from starlette.responses import Response, PlainTextResponse
import os

app = FastAPI()
app.include_router(settings_router)

origins = [
    os.environ.get("TRUSTED_HOST", "http://localhost"),
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def on_unauthorized_error(conn: HTTPConnection, exc: Exception) -> Response:
    return PlainTextResponse(str(exc), status_code=401)


app.add_middleware(AuthenticationMiddleware, backend=CustomAuthMiddleware(), on_error=on_unauthorized_error)


@app.get("/")
def index(storage: Storage = Depends(Storage)):
    count = storage.redis.incr("hits")
    return {"Hit me baby {} more time(s)".format(count)}
