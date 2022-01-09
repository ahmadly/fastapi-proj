from core.db import SessionLocal
from model import models, schemas

db = SessionLocal()


def get_item(item_id: int):
    return db.query(models.Data).filter(models.Data.id == item_id).first()


def get_items(skip: int = 0, limit: int = 100, year=None):
    _q = db.query(models.Data)
    if year:
        _q = _q.filter(models.Data.year == year)

    return _q.offset(skip).limit(limit).all()
