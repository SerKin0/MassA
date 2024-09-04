from fastapi import Request, APIRouter
from fastapi.responses import JSONResponse
import requests
from pydantic import TypeAdapter

from src.settings import API_WEATHER, BASE_URL
from src.models import WeatherData

router = APIRouter()


@router.post('/weather')
async def get_weather(request: Request):
    # Извлекаем json с данными из формы
    data = await request.json()
    # Записываем название города в переменную (если нет, то вводит None)
    city = data.get("city")
    # Если отправляем пустую форму, то возвращаем ошибку
    if not city:
        return JSONResponse(content={"error": "Город не указан"}, status_code=400)
    try:
        data = requests.get(
            BASE_URL,
            params={'q': city, 'type': 'like', 'units': 'metric', 'APPID': API_WEATHER, 'lang': 'ru'}
        ).json()

        print(f"{data=}")

        if data["cod"] != "200":
            return {"error": "Город не найден"}

        weather_data = TypeAdapter(WeatherData).validate_python(data)
        return {
            "temp": weather_data.list[0].main.temp,
            "feels_like": weather_data.list[0].main.feels_like,
            "description": weather_data.list[0].weather[0].description,
            "speed_wind": weather_data.list[0].wind.speed
        }

    except requests.RequestException as e:
        print(e)
        return {"error": str(e)}
