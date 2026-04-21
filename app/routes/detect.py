
from fastapi import APIRouter
from app.models.schemas import DetectRequest, DetectResponse
from app.services.detection_service import detect_emergency_logic
from app.services.twilio_service import send_sms, make_call
import time

router = APIRouter()

# 🔥 cooldown tracker
last_trigger_time = 0


# 🔥 reason generator (no LLM needed)
def generate_reason(text, volume, repeat_count):
    text = text.lower()
    reasons = []

    if "help" in text or "bachao" in text:
        reasons.append("distress keywords detected")

    if repeat_count > 1:
        reasons.append("repeated speech")

    if volume > 0.7:
        reasons.append("high voice intensity")

    return ", ".join(reasons)


@router.post("/detect-emergency", response_model=DetectResponse)
def detect_emergency(payload: DetectRequest):
    global last_trigger_time

    # Step 1: AI detection
    emergency, category, confidence = detect_emergency_logic(
        text=payload.text,
        volume=payload.volume,
        repeat_count=payload.repeat_count

    )
    # 🔥 FORCE TRIGGER (panic / shake)
    if payload.force_emergency:
     emergency = True
    category = "manual trigger"
    confidence = 1.0

    # 🔥 Step 2: cooldown check (prevent spam)
    if time.time() - last_trigger_time < 20:
        emergency = False

    # 🔥 Step 3: confidence filter
    if confidence < 0.6:
        emergency = False

    # 🔥 Step 4: If emergency → send SMS + CALL
    if emergency and payload.contacts:
        last_trigger_time = time.time()

        maps_link = f"https://maps.google.com/?q={payload.latitude},{payload.longitude}"

        # 🔥 explanation
        reason = generate_reason(
            payload.text,
            payload.volume,
            payload.repeat_count
        )

        sms_text = (
            f"🚨 Emergency detected!\n"
            f"Type: {category}\n"
            f"Reason: {reason}\n"
            f"Location: {maps_link}"
        )

        for contact in payload.contacts:
            try:
                send_sms(contact, sms_text)
                make_call(contact)
            except Exception as e:
                print(f"❌ Failed for {contact}: {e}")

    # Step 5: Response
    return DetectResponse(
        emergency=emergency,
        category=category,
        confidence=confidence,
        message="Emergency detected" if emergency else "No emergency detected"
    )