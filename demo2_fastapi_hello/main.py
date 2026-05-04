# простое fastapi приложение для демонстрации контейнеризации

from fastapi import FastAPI

app = FastAPI(
    title="Demo API",
    description="Демонстрационное API для практического занятия"
)


@app.get("/")
async def root():
    """корневой эндпоинт, возвращает приветствие"""
    return {"message": "Hello World"}


@app.get("/health")
async def health_check():
    """проверка работоспособности сервиса"""
    return {"status": "ok"}
