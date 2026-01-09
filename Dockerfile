# Используем официальный образ Python
FROM python:3.11-slim

# Устанавливаем системные зависимости для VLC и других библиотек
RUN apt-get update && apt-get install -y \
    vlc \
    libvlc-dev \
    libvlccore-dev \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY . .

# Создаем директорию для базы данных (если нужно)
RUN mkdir -p /app/data

# Устанавливаем переменные окружения для VLC (headless режим)
ENV VLC_PLUGIN_PATH=/usr/lib/vlc/plugins
ENV DISPLAY=:0

# Точка входа
CMD ["python", "main.py"]

