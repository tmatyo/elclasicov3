import os

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from backend.models import ImportDataRequest, get_db, create_tables
from backend.services import import_crawler_data, get_crawler_data, get_schedule_from_db, get_stats_from_db, get_fixtures_from_db
from contextlib import asynccontextmanager
from sqlmodel import Session


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield
    print('App closing')

allow_origins = os.getenv("ALLOW_ORIGINS", 'http://localhost:3000').split(',')

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def read_root():
    return {"status": "ok", "message": "Ready for your requests"}


@app.post("/import-data")
def import_data(data: ImportDataRequest, db: Session = Depends(get_db)):
    return import_crawler_data(data, db)


@app.get("/get-data")
def get_data(db: Session = Depends(get_db)):
    return get_crawler_data(db)


@app.get("/get-schedule")
def get_schedule(db: Session = Depends(get_db)):
    return get_schedule_from_db(db)


@app.get("/get-stat")
def get_stat(db: Session = Depends(get_db)):
    return get_stats_from_db(db)


@app.get("/get-fixture")
def get_fixture(db: Session = Depends(get_db)):
    return get_fixtures_from_db(db)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
