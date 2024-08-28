import os

from fastapi import Request, APIRouter
from fastapi.responses import JSONResponse
from dotenv import load_dotenv
import requests

router = APIRouter()
load_dotenv(".env")

api_key = os.environ['API_WEATHER']


@router.post('/weather')
async def get_weather(request: Request):
    # Принимаем json с данными формы
    data = await request.json()
    # Записываем название города в переменную (если нет, то вводит None)
    city = data.get("city")
    # Если отправляем пустую форму, то возвращаем ошибку
    if not city:
        return JSONResponse(content={"error": "Город не указан"}, status_code=400)

    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"

    try:
        response = requests.get(complete_url)
        print(f"{response=}")
        data = response.json()
        print(f"{data=}")

        if data["cod"] != "404":
            temp = data["main"]["temp"] - 273.15
            feels_like = data["main"]["feels_like"] - 273.15
            description = data["weather"][0]["description"]
            return {"temp": round(temp, 1), "feels_like": round(feels_like, 1), "description": description}
        else:
            return {"error": "Город не найден"}
    except requests.RequestException as e:
        return {"error": str(e)}
