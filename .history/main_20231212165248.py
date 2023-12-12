from fastapi import FastAPI
from routes.route import rout

app=FastAPI()

app.include_router(route)

