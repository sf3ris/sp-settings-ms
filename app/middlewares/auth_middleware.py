import requests
from os import environ
import typing
from fastapi import status
from fastapi.security import OAuth2PasswordBearer
from starlette.requests import HTTPConnection
from starlette.authentication import AuthenticationBackend, AuthCredentials, BaseUser, AuthenticationError

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='')


class CustomAuthMiddleware(AuthenticationBackend):

    async def authenticate(
            self, request: HTTPConnection
    ) -> typing.Optional[typing.Tuple["AuthCredentials", "BaseUser"]]:
        if request.get('method') == 'OPTIONS':
            return
        if "Authorization" not in request.headers:
            raise AuthenticationError('Header not found')
        auth = request.headers['Authorization']
        schema, token = auth.split()
        if schema != 'Bearer':
            raise AuthenticationError('Wrong Schema')

        endpoint = environ.get('AUTH_HOST', 'http://localhost') + '/validate'
        r = requests.post(
            endpoint,
            data={'access_token': token}
        )
        if r.status_code != status.HTTP_200_OK:
            raise AuthenticationError('Unauthorized')

        return
