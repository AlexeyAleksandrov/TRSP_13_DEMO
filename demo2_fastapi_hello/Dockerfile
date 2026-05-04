# базовый образ python alpine (облегченная версия)
FROM python:3.12-alpine

# переменные окружения
# отключаем создание .pyc файлов
ENV PYTHONDONTWRITEBYTECODE=1
# отключаем буферизацию вывода
ENV PYTHONUNBUFFERED=1

# рабочая директория
WORKDIR /usr/src/app

# копируем файл зависимостей
COPY requirements.txt .

# обновляем pip и устанавливаем зависимости
RUN pip install --upgrade pip && pip install -r requirements.txt

# копируем исходный код приложения
COPY . .

# команда запуска uvicorn сервера
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
