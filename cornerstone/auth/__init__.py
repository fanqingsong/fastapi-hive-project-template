
from cornerstone.auth.db import create_db_and_tables
from cornerstone.auth.router import register_auth_router
from fastapi import FastAPI
from fastapi_hive.ioc_framework.cornerstone_model import CornerstoneHooks, CornerstoneAsyncHooks


__all__ = ['CornerstoneHooksImpl', 'CornerstoneAsyncHooksImpl']


class CornerstoneHooksImpl(CornerstoneHooks):

    def __init__(self, app: FastAPI):
        super(CornerstoneHooksImpl, self).__init__(app)

    def pre_endpoint_setup(self):
        print("call pre setup from cornerstone!!!")

    def post_endpoint_setup(self):
        print("call post setup from cornerstone!!!")

        register_auth_router(self._app)

    def pre_endpoint_teardown(self):
        print("call pre teardown from cornerstone!!!")

    def post_endpoint_teardown(self):
        print("call pre teardown from cornerstone!!!")


class CornerstoneAsyncHooksImpl(CornerstoneAsyncHooks):

    def __init__(self, app: FastAPI):
        super(CornerstoneAsyncHooksImpl, self).__init__(app)

    async def pre_endpoint_setup(self):
        print("call pre setup from cornerstone async!!!")

        await create_db_and_tables()

    async def post_endpoint_setup(self):
        print("call post setup from cornerstone async!!!")

    async def pre_endpoint_teardown(self):
        print("call pre teardown from cornerstone async!!!")

    async def post_endpoint_teardown(self):
        print("call pre teardown from cornerstone async!!!")

