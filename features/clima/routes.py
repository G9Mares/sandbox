from fastapi import APIRouter, Body, Request
from .service import service_get_weather_history, service_get_weather_city, service_new_history_record


router =  APIRouter(prefix="")




@router.get("/history")
def get_weather_history():
    try:
        history = service_get_weather_history()
        return {"status":200, "data":history}

    except Exception as e:
        print(e)
        return {"status":500, "error":"Ocurrio un error inesperado con la base de datos"}
    
@router.get("/weather")
async def get_weather_city(city:str, request:Request):
    ip = request.client.host
    if not city:
        return {"status":400, "error":"Ciudad no valida"}
    weathe_data = await  service_get_weather_city(city=city, ip = ip)
    if not weathe_data:
        return {"status":400, "error":"Ocurrio un error inesperado con el servicio, verifique la ciudad"}
    create_history = service_new_history_record(weather_info=weathe_data)
    if request.method == "POST":
        return {"status":200, "message":f"Registro de la ciudad {city} creado con exito"}
    return {"status":200, "data": weathe_data}

    

    
@router.post("/history")
async def crete_new_history_record(request:Request, city:str):
   data = await get_weather_city(city=city, request=request)
   return data