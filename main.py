import uvicorn
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates

from src.router import router as router_weather


app = FastAPI()
templates = Jinja2Templates(directory='templates')
app.include_router(router_weather)


@app.get('/')
async def welcome_page(request: Request):
    return templates.TemplateResponse('welcome.html', {'request': request})


@app.get('/weather')
async def weather_page(request: Request):
    return templates.TemplateResponse('weather.html', {'request': request})


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
