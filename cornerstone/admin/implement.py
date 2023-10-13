
from sqlalchemy import create_engine
from sqladmin import Admin
from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request
import httpx
import logging
from fastapi import FastAPI
from config.config import settings


DATABASE_URL = settings.get("DATABASE_URL")
print(f"!!! DATABASE_URL = {DATABASE_URL}")

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
)


class AdminAuth(AuthenticationBackend):
    async def login(self, request: Request) -> bool:
        form = await request.form()
        username, password = form["username"], form["password"]

        async with httpx.AsyncClient() as client:
            data = {'username': username, 'password': password}
            response = await client.post('http://localhost:8000/auth/jwt/login', data=data)
            print(response)
            print(response.text)
            print(response.json())
            # print(response.json()['detail'])

            resp_json = response.json()

            if resp_json.get('detail') == 'LOGIN_BAD_CREDENTIALS':
                print('longin failed.')
                return False

        # Validate username/password credentials
        # And update session
        token = resp_json.get('access_token')

        logging.info(f'login token = {token}')

        request.session.update({"token": token})

        return True

    async def logout(self, request: Request) -> bool:
        # Usually you'd want to just clear the session
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        logging.info(f'auth token = {token}')

        if not token:
            return False

        # Check the token in depth
        return True


authentication_backend = AdminAuth(secret_key="secret_key")


def create_admin_container(app: FastAPI):
    admin = Admin(app, engine, authentication_backend=authentication_backend)
    return admin


