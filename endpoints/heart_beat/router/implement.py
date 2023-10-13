import logging

from fastapi import APIRouter, Request, FastAPI
from cornerstone.auth.users import current_active_user
from cornerstone.auth.db import User
from endpoints.heart_beat.schema.heartbeat import HearbeatResult
from fastapi import Depends
import databases

router = APIRouter()


@router.get("/heartbeat", response_model=HearbeatResult, name="heartbeat")
async def get_hearbeat(request: Request) -> HearbeatResult:
    logging.info("====== request ========")
    logging.info(request)

    logging.info("====== request.app ========")
    logging.info(request.app)

    logging.info("========== app state ====")
    logging.info(request.app.state)
    logging.info(request.app.state.db_flag)

    logging.info("========== request state ====")
    request.state.db_flag = True
    logging.info(request.state)
    logging.info(request.state.db_flag)


    db: databases.Database = request.app.state.db

    query = "SELECT * FROM notes"
    rows = await db.fetch_all(query=query)
    logging.info("=== notes ===========")
    print('notes:', rows)

    heartbeat = HearbeatResult(is_alive=True)
    return heartbeat


@router.get("/authenticated_echo")
async def authenticated_echo(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}