from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware
from api import router as api_router

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATABASE_URI = 'postgresql://postgres:postgres@localhost/inshorts'

app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URI)
app.include_router(api_router)