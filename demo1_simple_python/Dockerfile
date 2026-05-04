# базовый образ python
FROM python:3.12-slim

# метаданные образа
LABEL maintainer="student"

# рабочая директория внутри контейнера
WORKDIR /usr/src/app

# копируем скрипт в контейнер
COPY main.py ./

# команда запуска при старте контейнера
CMD ["python", "./main.py"]
