from fastapi import FastAPI

from app.core.db.database import engine
from app.http.controllers.v1 import router as v1router
from app.persistence.models import Base as modelBase
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

modelBase.metadata.create_all(bind=engine)

app.include_router(v1router, prefix='/api')
