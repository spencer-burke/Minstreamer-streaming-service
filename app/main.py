from fastapi import FastAPI
from .routers import filmstreaming

app = FastAPI()
app.include_router(filmstreaming.router)
