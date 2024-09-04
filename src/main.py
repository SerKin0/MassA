from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from src.router import router as router_weather
from logger.logger import logger as log

app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.include_router(router_weather)


@app.get('/')
async def welcome_page(request: Request):
    log.debug("Запуске приветственной страницы.")
    return templates.TemplateResponse('welcome.html', {'request': request})


@app.get('/weather')
async def weather_page(request: Request):
    log.debug("Запуск страницы с данными погоды.")
    return templates.TemplateResponse('weather.html', {'request': request})
