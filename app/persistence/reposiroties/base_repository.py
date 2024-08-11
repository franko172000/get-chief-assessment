from typing import TypeVar, cast

from fastapi import HTTPException
from starlette import status

from app.core.db.db_session_context import DBSessionContext

T = TypeVar("T")


class BaseRepository(DBSessionContext):
    _model: T
    __abstract__ = True

    def find_or_fail_by_id(self, resource_id: int) -> T:
        result = self.db.query(self._model).filter(self._model.id == resource_id).first()
        if not result:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Resource not found')
        return cast(T, result)
