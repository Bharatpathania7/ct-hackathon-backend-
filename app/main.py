# from fastapi import FastAPI
# from app.routes.detect import router as detect_router
#
# app = FastAPI(title="SLM Backend")
#
# app.include_router(detect_router)
#
#
# @app.get("/")
# def home():
#     return {"message": "FastAPI running successfully 🚀"}
from fastapi import FastAPI
import asyncio

from app.routes.detect import router as detect_router
from app.routes.timer import router as timer_router
from app.services.timer_service import check_timers

# ✅ First create app
app = FastAPI(title="SLM Backend")

# ✅ Then include routers
app.include_router(detect_router)
app.include_router(timer_router)

# ✅ Home route
@app.get("/")
def home():
    return {"message": "FastAPI running successfully 🚀"}

# ✅ Startup event
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(check_timers())