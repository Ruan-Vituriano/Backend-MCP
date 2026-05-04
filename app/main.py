from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.chat_route import router as chat_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_credentials=True,
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

app.include_router(chat_router)
