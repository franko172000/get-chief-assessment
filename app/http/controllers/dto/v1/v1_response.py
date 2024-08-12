from typing import Optional

from pydantic import BaseModel


class AppV1Response(BaseModel):
    data: Optional[object] = None
    message: Optional[str] = None
