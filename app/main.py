import os
from fastapi import FastAPI
from .routers import filmstreaming
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(filmstreaming.router)
