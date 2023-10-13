
from sqlalchemy import Column, Integer, String, Boolean

from sqladmin import Admin, ModelView

from cornerstone.db import Base


class Notes(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True)
    text = Column(String)
    completed = Column(Boolean)


class NotesAdmin(ModelView, model=Notes):
    column_list = [Notes.id, Notes.text, Notes.completed]


def add_to_admin():
    from cornerstone.admin import admin

    admin.add_view(NotesAdmin)
