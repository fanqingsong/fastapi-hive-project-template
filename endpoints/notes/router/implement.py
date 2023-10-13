
from fastapi import APIRouter
from fastapi_crudrouter import SQLAlchemyCRUDRouter, DatabasesCRUDRouter

from endpoints.notes.schema.pydantic import NoteIn, Note
from endpoints.notes.db.implement import Notes

from cornerstone.db import database

router = APIRouter()


@router.get("/NoteGet", response_model=Note, name="NoteGet")
def get_hearbeat() -> Note:
    ret = Note(text="jkk")
    return ret


crudrouter = DatabasesCRUDRouter(
    schema=Note,
    create_schema=NoteIn,
    database=database,
    table=Notes.__table__,
    prefix='note_data',
    # dependencies=[Depends(current_active_user)]
)

router.include_router(crudrouter)

print("--- call notes router over -----")
