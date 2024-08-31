from starlette.config import Config

config = Config(".env")

BASE_URL = config("BASE_URL")
API_WEATHER = config("API_WEATHER")
BACKEND_INSIDE_PORT = config("BACKEND_INSIDE_PORT")
BACKEND_OUTSIDE_PORT = config("BACKEND_OUTSIDE_PORT")