from fastapi import FastAPI
from app.routes.chat_route import router as chat_router

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

app.include_router(chat_router)
