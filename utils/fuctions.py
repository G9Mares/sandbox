import httpx

async def consume_external_api(url:str, method)->bool|dict:
    try:
        async with httpx.AsyncClient() as client:
            if not hasattr(client,method):
                return False
            metodo = getattr(client,method)
            respuesta = await metodo(url)
            return respuesta.json()
    except Exception as e:
        print(e)
        return False