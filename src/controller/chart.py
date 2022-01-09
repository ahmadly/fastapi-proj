from core.db import SessionLocal
from model import models, schemas

db = SessionLocal()


def get_chart(chart_id: int):
    return db.query(models.Chart).filter(models.Chart.id == chart_id).first()
