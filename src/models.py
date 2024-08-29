from pydantic import BaseModel
from typing import List, Optional


class Coord(BaseModel):
    lat: float
    lon: float


class Main(BaseModel):
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int
    sea_level: int
    grnd_level: int


class Wind(BaseModel):
    speed: float
    deg: int


class Clouds(BaseModel):
    all: int


class Weather(BaseModel):
    id: int
    main: str
    description: str
    icon: str


class Sys(BaseModel):
    country: str


class ListWeather(BaseModel):
    id: int
    name: str
    coord: Coord
    main: Main
    dt: int
    wind: Wind
    sys: Sys
    rain: Optional[float] = None
    snow: Optional[float] = None
    clouds: Clouds
    weather: List[Weather]

    def __init__(self, **data):
        super().__init__(**data)
        # Округляем числа с плавающей точкой
        self.main.temp = round(self.main.temp, 1)
        self.main.feels_like = round(self.main.feels_like, 1)
        self.wind.speed = round(self.wind.speed, 1)


class WeatherData(BaseModel):
    message: str
    cod: str
    count: int
    list: List[ListWeather]

