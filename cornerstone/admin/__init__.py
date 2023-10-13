
from fastapi import FastAPI
from fastapi_hive.ioc_framework.cornerstone_model import CornerstoneHooks, CornerstoneAsyncHooks
from cornerstone.admin.implement import create_admin_container

__all__ = ['admin', 'CornerstoneHooksImpl', 'CornerstoneAsyncHooksImpl']


admin = None


class CornerstoneHooksImpl(CornerstoneHooks):

    def __init__(self, app: FastAPI):
        super(CornerstoneHooksImpl, self).__init__(app)

    def pre_endpoint_setup(self):
        print("call pre setup from cornerstone!!!")

        # print("+++++++++++++++++++1111")
        # print(locals())
        #
        # print("+++++++++++++++++++2222")
        # print(globals())

        globals()['admin'] = create_admin_container(self._app)

    def post_endpoint_setup(self):
        print("call post setup from cornerstone!!!")

        # print("+++++++++++++++++++3333")
        # print(globals()['admin'])

    def pre_endpoint_teardown(self):
        print("call pre teardown from cornerstone!!!")

    def post_endpoint_teardown(self):
        print("call pre teardown from cornerstone!!!")


class CornerstoneAsyncHooksImpl(CornerstoneAsyncHooks):

    def __init__(self, app: FastAPI):
        super(CornerstoneAsyncHooksImpl, self).__init__(app)

    async def pre_endpoint_setup(self):
        print("call pre setup from cornerstone async!!!")

    async def post_endpoint_setup(self):
        print("call post setup from cornerstone async!!!")

    async def pre_endpoint_teardown(self):
        print("call pre teardown from cornerstone async!!!")

    async def post_endpoint_teardown(self):
        print("call pre teardown from cornerstone async!!!")

