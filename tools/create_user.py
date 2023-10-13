import contextlib

import path
import sys
 
# directory reach
directory = path.Path(__file__).abspath()
print(directory)
 
# setting path
sys.path.append(directory.parent.parent)


from auth.db import get_async_session, get_user_db
from cornerstone.auth.schemas import UserCreate
from auth.users import get_user_manager
from fastapi_users.exceptions import UserAlreadyExists



get_async_session_context = contextlib.asynccontextmanager(get_async_session)
get_user_db_context = contextlib.asynccontextmanager(get_user_db)
get_user_manager_context = contextlib.asynccontextmanager(get_user_manager)


async def create_user(email: str, password: str, is_superuser: bool = False):
    try:
        async with get_async_session_context() as session:
            async with get_user_db_context(session) as user_db:
                async with get_user_manager_context(user_db) as user_manager:
                    user = await user_manager.create(
                        UserCreate(
                            email=email, password=password, is_superuser=is_superuser
                        )
                    )
                    print(f"User created {user}")
    except UserAlreadyExists:
        print(f"User {email} already exists")




import asyncio

if __name__ == "__main__":
  asyncio.run(create_user("king.arthur@camelot.bt", "guinevere"))
  




