from pydantic import BaseModel
from typing import Optional

# Container Params Model
class ContainerParams(BaseModel):
    container_type: str
    description: str
    empty: bool
    name: str
    robot: str

# JSON-RPC Request Model
class ContainersModel(BaseModel):
    id: int
    jsonrpc: str
    method: str
    params: Optional[dict] = None