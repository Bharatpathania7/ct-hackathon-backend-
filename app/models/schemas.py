# from typing import List, Optional
# from pydantic import BaseModel
#
#
# class DetectRequest(BaseModel):
#     user_id: str
#     text: str
#     volume: float
#     repeat_count: int
#     latitude: float
#     longitude: float
#     contacts: Optional[List[str]] = None
#     force_emergency: Optional[bool] = False
#
#
#
# class DetectResponse(BaseModel):
#     emergency: bool
#     category: str
#     confidence: float
#     message: str


from typing import List, Optional
from pydantic import BaseModel, Field

# ---------------- TIMER ----------------

class TimerStartRequest(BaseModel):
    user_id: str
    duration: int = Field(..., gt=0, lt=3600, description="Duration in seconds")


class TimerCancelRequest(BaseModel):
    user_id: str


class TimerResponse(BaseModel):
    status: str
    message: str


# ---------------- DETECTION ----------------

class DetectRequest(BaseModel):
    user_id: str
    text: str
    volume: float = Field(..., ge=0, le=1, description="Audio volume (0 to 1)")
    repeat_count: int = Field(..., ge=1, description="Keyword repeat count")
    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)
    contacts: Optional[List[str]] = None
    force_emergency: Optional[bool] = False


class DetectResponse(BaseModel):
    emergency: bool
    category: str
    confidence: float
    message: str