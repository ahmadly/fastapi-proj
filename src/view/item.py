from fastapi import APIRouter, HTTPException

from controller.item import get_item, get_items
from core.worker import celery
from model import schemas

router = APIRouter(
    prefix='/items',
    tags=['items'],
    responses={404: {'description': 'Not found'}},
)


@router.get('/', response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, year: str | None = None):
    items: list = get_items(skip=skip, limit=limit, year=year)
    return items


@router.get('/{item_id}', response_model=schemas.Item)
def read_item(item_id: int):
    item = get_item(item_id=item_id)

    if item is None:
        raise HTTPException(status_code=404, detail='Item not found')

    item.chart_id = str(celery.send_task('create_chart_task', kwargs={'item_id': item_id}))
    return item
