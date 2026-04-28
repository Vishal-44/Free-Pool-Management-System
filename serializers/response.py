from pydantic import BaseModel
from typing import Optional

class APIResponse(BaseModel):
    message: str
    data: Optional[dict] = None
