# простое fastapi приложение

from fastapi import FastAPI

app = FastAPI(
    title="Demo API",
    description="TRSP_13_DEMO"
)


@app.get("/")
async def root():
    """корневой эндпоинт, возвращает приветствие"""
    return {"message": "Hello World"}


@app.get("/health")
async def health_check():
    """проверка работоспособности сервиса"""
    return {"status": "ok"}
