from fastapi import FastAPI
from routes.route import ro

app=FastAPI()

app.include_router(route)

