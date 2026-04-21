import time
import asyncio
from app.services.twilio_service import send_sms, make_call

active_timers = {}

def start_timer(user_id: str, duration: int):
    end_time = time.time() + duration

    active_timers[user_id] = {
        "end_time": end_time,
        "is_active": True
    }

    print(f"[TIMER STARTED] User: {user_id}, Ends at: {end_time}")

    return {
        "status": "success",
        "message": "Timer started"
    }


def cancel_timer(user_id: str):
    if user_id in active_timers:
        active_timers[user_id]["is_active"] = False

        print(f"[TIMER CANCELLED] User: {user_id}")

        return {
            "status": "success",
            "message": "Timer cancelled"
        }

    return {
        "status": "error",
        "message": "No active timer"
    }


async def check_timers():
    while True:
        now = time.time()

        for user_id, timer in list(active_timers.items()):
            if timer["is_active"] and now >= timer["end_time"]:

                print(f"[SOS TRIGGERED] Timer expired for user: {user_id}")

                # 🔥 Trigger SOS
                send_sms()
                make_call()

                timer["is_active"] = False
                active_timers.pop(user_id, None)

        await asyncio.sleep(2)