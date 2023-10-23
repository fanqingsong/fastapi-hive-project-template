
import logging

from fastapi import FastAPI
from fastapi_hive.ioc_framework import IoCFramework

app = FastAPI()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

ioc_framework = IoCFramework(app)

ioc_framework.config.API_PREFIX = '/v1'
ioc_framework.config.ENDPOINT_PACKAGE_PATHS = ["./endpoints"]
# logger.info("-----------------------------------------------------")
# logger.info(dir(ioc_framework))
# logger.info(dir(ioc_framework.config))
ioc_framework.config.HIDE_ENDPOINT_CONTAINER_IN_API = True
ioc_framework.config.HIDE_ENDPOINT_IN_API = False


def pre_setup():
    print("------ call pre setup ----")


ioc_framework.config.PRE_ENDPOINT_SETUP = pre_setup


def post_setup():
    print("------ call post setup ----")


ioc_framework.config.POST_ENDPOINT_SETUP = post_setup


async def async_pre_setup():
    print("------ call async pre setup ----")


ioc_framework.config.ASYNC_PRE_ENDPOINT_SETUP = async_pre_setup


async def async_post_teardown():
    print("------ call async post teardown ----")

ioc_framework.config.ASYNC_POST_ENDPOINT_TEARDOWN = async_post_teardown

ioc_framework.init_modules()

