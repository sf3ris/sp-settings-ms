import os
import typing
from fastapi.testclient import TestClient
from starlette.requests import HTTPConnection
from app.middlewares.auth_middleware import CustomAuthMiddleware

from app.main import app

client = TestClient(app)


def authenticate_mock(request: HTTPConnection) -> typing.Optional[typing.Tuple["AuthCredentials", "BaseUser"]]:
    return


def test_index_should_return_unauthorized():
    response = client.get("/")
    assert response.status_code == 401
