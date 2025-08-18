from controllers.postgres_controller import Postgres_Controller
import os
from dotenv import load_dotenv
from .model import Weather, Base
from utils.fuctions import consume_external_api
from uuid import uuid4

load_dotenv()
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

controller = Postgres_Controller(
    usuario=os.getenv("POSTGRES_USER"),
    passw=os.getenv("POSTGRES_PASSWORD"),
    puerto=os.getenv("PORT_DB"),
    host=os.getenv("HOST_DB"),
    db="mvs_db",
)

#controller.create_model(Base=Base)


def service_get_weather_history():
    return controller.get_all(Weather)

def service_new_history_record(weather_info:dict):
    try:
        return controller.create_record(Weather,weather_info)
    except Exception as e:
        print("Error al crear el historial",e)
        return False

async def service_get_weather_city(city:str, ip:str):
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHER_API_KEY}&q={city}&aqi=no"
    data = await consume_external_api(url=url,method="get")
    if not data:
        return False
    if data.get("error"):
        return False
    weather_data = {
        "id":f"query-{str(uuid4())}",
        "source_query":ip,
        "country": data.get("location",{}).get("country","Sin informacion"),
        "city":data.get("location",{}).get("name","Sin informacion"),
        "region":data.get("location",{}).get("region","Sin informacion"),
        "temp_c":data.get("current",{}).get("temp_c","Sin informacion"),
        "condition":data.get("current",{}).get("condition",{}).get("text","Sin informacion"),
        "humidity":data.get("current",{}).get("humidity","Sin informacion"),
        "wind_kph":data.get("current",{}).get("wind_kph","Sin informacion")
    }
    return weather_data


