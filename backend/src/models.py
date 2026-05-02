from datetime import datetime, timezone
from typing import List, Optional
import os
from sqlmodel import Field, Session, SQLModel, create_engine

DB_HOST = os.getenv("DB_HOST", 'localhost')
DB_USER = os.getenv("DB_USER", "root")
DB_PASS = os.getenv("DB_PASS", "")
DB_NAME = os.getenv("DB_NAME", "elclasico")

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:3306/{DB_NAME}"
engine = create_engine(DATABASE_URL)


class Schedule(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    time: str
    time_parsed: str
    home_team: str
    away_team: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc))


class Stat(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    matches: int
    barca: int
    barca_goals: int
    draw: int
    real: int
    real_goals: int
    avg_attendance: float
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc))


class Fixture(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    date: str
    home_team: str
    away_team: str
    event: str
    score: str
    winner: str
    attendance: str
    link: str
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc))


class ImportDataRequest(SQLModel):
    schedules: Optional[List[Schedule]] = []
    stats: Optional[List[Stat]] = []
    fixtures: Optional[List[Fixture]] = []

class ResponseDataRequest(SQLModel):
    schedules: List[Schedule] = []
    stats: List[Stat] = []
    fixtures: List[Fixture] = []

def get_db():
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()


def create_tables():
    SQLModel.metadata.create_all(engine)
