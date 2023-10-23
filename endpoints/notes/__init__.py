
from fastapi import FastAPI
from fastapi_hive.ioc_framework.endpoint_hooks import EndpointHooks, EndpointAsyncHooks
from endpoints.notes.db import add_to_admin


class EndpointHooksImpl(EndpointHooks):

    def __init__(self):
        super(EndpointHooksImpl, self).__init__()

    def setup(self):
        print("call pre setup from EndpointImpl!!!")
        # print("---- get fastapi app ------")
        # print(self._app)

        add_to_admin()

    def teardown(self):
        print("call pre teardown from EndpointImpl!!!")


class EndpointAsyncHooksImpl(EndpointAsyncHooks):

    def __init__(self):
        super(EndpointAsyncHooksImpl, self).__init__()

    async def setup(self):
        print("call pre setup from cornerstone EndpointAsyncImpl!!!")

    async def teardown(self):
        print("call pre teardown from cornerstone EndpointAsyncImpl!!!")



