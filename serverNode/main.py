from fastapi import FastAPI
from routers import getUserInfo, wireguardCurrent

app = FastAPI()
app.include_router(getUserInfo.router)
app.include_router(wireguardCurrent.router)
