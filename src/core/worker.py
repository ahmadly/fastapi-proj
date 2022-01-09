import os

import plotly.express as px
import requests
from celery import Celery
from sqlalchemy import func

from controller.item import get_item
from core.db import SessionLocal
from core.utils import SETTINGS
from model.models import Data

db = SessionLocal()

celery = Celery(
    'core',
    broker=SETTINGS.CELERY_BROKER_URL,
    backend=SETTINGS.CELERY_RESULT_BACKEND,
)


@celery.task(bind=True, name='load_data_task', max_retries=3)
def load_data_task(self):
    # bypass if data already exist
    if not db.query(func.count(Data.id)).scalar() > 0:
        try:
            with requests.get(url=SETTINGS.DATASET_ENDPOINT) as response:
                objects = []
                if not response.ok:
                    raise

                for row in response.json()['data']:
                    _cleaned = []
                    for i in row[8:]:
                        if i in ['No Data', 's', ' ']:
                            _cleaned.append(None)
                        else:
                            _cleaned.append(i)

                    objects.append(Data(**dict(zip(SETTINGS.DATASET_FIELDS, _cleaned))))
                db.add_all(objects)
                db.commit()
        except Exception as exc:
            raise self.retry(exc=exc, countdown=2 ** self.request.retries)


@celery.task(bind=True, name='create_chart_task')
def create_chart_task(self, item_id):
    item = get_item(item_id=item_id)
    x = ['grade_k', 'grade_1', 'grade_2', 'grade_3', 'grade_4', 'grade_5', 'grade_6', 'grade_7', 'grade_8']
    y = [item.grade_k, item.grade_1, item.grade_2, item.grade_3, item.grade_4, item.grade_5, item.grade_6,
         item.grade_7, item.grade_8]
    fig = px.bar(x=x, y=y)
    fig.write_html(f'charts/{self.request.id}.html')
