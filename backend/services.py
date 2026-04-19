from backend.models import ImportDataRequest, Schedule, Stat, Fixture, ResponseDataRequest
from sqlmodel import Session, select
from fastapi import HTTPException
from typing import List


def import_crawler_data(data: ImportDataRequest, db: Session):
    """
    Import crawler data into the database
    """
    try:
        imported_counts = {
            "schedules": 0,
            "stats": 0,
            "fixtures": 0
        }

        if len(data.schedules) > 0:
            for schedule_data in data.schedules:
                schedule = Schedule(**schedule_data.dict())
                db.add(schedule)
                imported_counts["schedules"] += 1

        if len(data.stats) > 0:
            for stat_data in data.stats:
                stat = Stat(**stat_data.dict())
                db.add(stat)
                imported_counts["stats"] += 1

        if len(data.fixtures) > 0:
            for fixture_data in data.fixtures:
                fixture = Fixture(**fixture_data.dict())
                db.add(fixture)
                imported_counts["fixtures"] += 1

        db.commit()

        return {
            "status": "Success",
            "message": "Data imported successfully",
            "imported": imported_counts
        }

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Import failed: {str(e)}")


def get_schedule_from_db(db: Session) -> List[Schedule]:
    """
    Get schedule data from DB
    """
    try:
        return db.exec(select(Schedule)).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"There was a problem with obtaining crawler data: {e}")


def get_stats_from_db(db: Session) -> List[Stat]:
    """
    Get stats data from DB
    """
    try:
        return db.exec(select(Stat)).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"There was a problem with obtaining crawler data: {e}")


def get_fixtures_from_db(db: Session) -> List[Fixture]:
    """
    Get fixtures data from DB
    """
    try:
        return db.exec(select(Fixture)).all()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"There was a problem with obtaining crawler data: {e}")


def get_crawler_data(db: Session) -> ResponseDataRequest:
    """
    Get crawler data from DB
    """
    return {
        "schedule": get_schedule_from_db(db),
        "stats": get_stats_from_db(db),
        "fixtures": get_fixtures_from_db(db)
    }
