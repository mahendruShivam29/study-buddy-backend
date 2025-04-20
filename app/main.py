from fastapi import FastAPI
from app.api import routes_upload, routes_generate

app = FastAPI()

app.include_router(routes_upload.router)
app.include_router(routes_generate.router)
