from fastapi import FastAPI
from config import settings

# from src.api.v1.order import order_router_v1

app = FastAPI(
    title=settings.PROJECT_NAME,
)

# app.include_router(order_router_v1)


# @app.get("/")
# def health():
#     return {"msg": "Hello World!"}
