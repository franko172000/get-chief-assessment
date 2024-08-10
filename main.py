from fastapi import FastAPI
from app.routes import v1 as v1routes
from app.config.database import create_tables
app = FastAPI()

create_tables()

app.include_router(v1routes.router)
