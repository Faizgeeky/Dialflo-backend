from pydantic import BaseModel
from typing import Optional
from enum import Enum
# from typing import List


class Status(Enum):
    Success = "Success"
    Failed = "Failed"


# AI support agent endpoit schemas
class UserQuery(BaseModel):
    query : str
    username: Optional[str] = None
    phone : Optional[str] = None