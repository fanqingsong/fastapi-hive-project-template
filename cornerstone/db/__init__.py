import logging

from fastapi_hive.ioc_framework.cornerstone_hooks import CornerstoneHooks, CornerstoneAsyncHooks
from cornerstone.db.implement import Base, database, create_all_tables
from fastapi import FastAPI

__all__ = ['Base', 'CornerstoneHooksImpl', 'CornerstoneAsyncHooksImpl']


class CornerstoneHooksImpl(CornerstoneHooks):

    def __init__(self):
        super(CornerstoneHooksImpl, self).__init__()

    def pre_endpoint_setup(self):
        print("call pre setup from cornerstone db!!!")

    def post_endpoint_setup(self):
        print("call post setup from cornerstone!!!")
        create_all_tables(self.app)

    def pre_endpoint_teardown(self):
        print("call pre teardown from cornerstone!!!")

    def post_endpoint_teardown(self):
        print("call pre teardown from cornerstone!!!")


class CornerstoneAsyncHooksImpl(CornerstoneAsyncHooks):

    def __init__(self):
        super(CornerstoneAsyncHooksImpl, self).__init__()

    async def pre_endpoint_setup(self):
        print("call pre setup from cornerstone async!!!")

        await database.connect()

    async def post_endpoint_setup(self):
        print("call post setup from cornerstone async!!!")

    async def pre_endpoint_teardown(self):
        print("call pre teardown from cornerstone async!!!")

    async def post_endpoint_teardown(self):
        print("call pre teardown from cornerstone async!!!")

        await database.disconnect()
