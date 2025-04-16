FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .

# Creamos directorio para almacenar mensajes
RUN mkdir -p /data

# Exponemos puerto 5000
EXPOSE 5000

CMD ["python", "app.py"]