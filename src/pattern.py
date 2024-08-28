from pydantic import BaseModel
from time import asctime


class Weather(BaseModel):
    time: str
