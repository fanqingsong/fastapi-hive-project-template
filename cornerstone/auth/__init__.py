
from cornerstone.auth.db import create_db_and_tables
from cornerstone.auth.router import register_auth_router
from fastapi import FastAPI
from fastapi_hive.ioc_framework.cornerstone_hooks import CornerstoneHooks, CornerstoneAsyncHooks


__all__ = ['CornerstoneHooksImpl', 'CornerstoneAsyncHooksImpl']


class CornerstoneHooksImpl(CornerstoneHooks):

    def __init__(self):
        super(CornerstoneHooksImpl, self).__init__()

    def pre_endpoint_setup(self):
        print("call pre setup from cornerstone!!!")

    def post_endpoint_setup(self):
        print("call post setup from cornerstone!!!")

        register_auth_router(self.app)

    def pre_endpoint_teardown(self):
        print("call pre teardown from cornerstone!!!")

    def post_endpoint_teardown(self):
        print("call pre teardown from cornerstone!!!")


class CornerstoneAsyncHooksImpl(CornerstoneAsyncHooks):

    def __init__(self):
        super(CornerstoneAsyncHooksImpl, self).__init__()

    async def pre_endpoint_setup(self):
        print("call pre setup from cornerstone async!!!")

        await create_db_and_tables()

    async def post_endpoint_setup(self):
        print("call post setup from cornerstone async!!!")

    async def pre_endpoint_teardown(self):
        print("call pre teardown from cornerstone async!!!")

    async def post_endpoint_teardown(self):
        print("call pre teardown from cornerstone async!!!")

