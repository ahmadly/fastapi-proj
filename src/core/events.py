import logging
import time

from core.db import Base, engine
from core.worker import celery


async def init_db():
    logging.info('init_db calling...')
    time.sleep(5)  # wait for db service
    Base.metadata.create_all(bind=engine)
    logging.info('init_db done.')


async def load_db():
    celery.send_task('load_data_task')
    logging.info('load_db called as background task')
