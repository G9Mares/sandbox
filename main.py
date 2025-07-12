from fastapi import FastAPI
from features.users import routes as user_service

app = FastAPI()
app.include_router(router=user_service.router)

@app.get("/")
def get_users():
    return []