import logging
import logging.config

from fastapi import FastAPI

from core.db import SessionLocal
from core.events import init_db, load_db
from core.utils import SETTINGS
from view import chart, item

logging.config.dictConfig({
    "version": 1,
    "formatters": {
        "default": {
            "format": "%(asctime)s - %(process)s - %(name)s - %(levelname)s - %(message)s"
        }
    },
    "handlers": {
        "console": {
            "formatter": "default",
            "class": "logging.StreamHandler",
            "stream": "ext://sys.stdout",
            "level": "DEBUG"
        }
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG"
    },
    "loggers": {
        "gunicorn": {
            "propagate": True
        },
        "uvicorn": {
            "propagate": True
        },
        "uvicorn.access": {
            "propagate": True
        }
    }
})


def get_application():
    logging.info('initializing app')
    _app = FastAPI(
        debug=SETTINGS.DEBUG,
        on_startup=[init_db, load_db],
    )

    _app.include_router(item.router)
    _app.include_router(chart.router)
    _app.db = SessionLocal()
    logging.info('app is ready')
    return _app
