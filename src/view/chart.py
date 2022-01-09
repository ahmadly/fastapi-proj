from fastapi import APIRouter, FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(
    prefix='/charts',
    tags=['charts'],
    responses={404: {'description': 'Not found'}},
)

templates = Jinja2Templates(directory='charts')


@router.get('/{chart_id}', response_class=HTMLResponse)
def read_chart(request: Request, chart_id: str):
    return templates.TemplateResponse(f"{chart_id}.html", {"request": request})
