from fastapi import APIRouter
from app.services.timer_service import start_timer, cancel_timer
from app.models.schemas import TimerStartRequest, TimerCancelRequest, TimerResponse

# ✅ Assign router properly
router = APIRouter(prefix="/timer", tags=["Timer"])

@router.post("/start", response_model=TimerResponse)
def start(req: TimerStartRequest):
    return start_timer(req.user_id, req.duration)

@router.post("/cancel", response_model=TimerResponse)
def cancel(req: TimerCancelRequest):
    return cancel_timer(req.user_id)