# Используется базовый образ Python 3.12 с минимальным размером
FROM python:3.12-slim
# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app
COPY . .
# Копирует файл requirements.txt в контейнер
COPY requirements.txt .
# Устанавливает зависимости из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Запуск приложения со Starlette с помощью uvicorn
CMD ["python", "src/main.py"]
EXPOSE 9800