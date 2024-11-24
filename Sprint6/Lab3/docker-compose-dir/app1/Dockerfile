FROM python:3.8-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# necesario para la verificación nc en healthcheck, posteriormente se elimina para que no pese tanto la imagen
# https://docs.docker.com/build/building/best-practices/#sort-multi-line-arguments
RUN apt-get update && \
    apt-get install -y netcat-openbsd && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 5000
COPY app.py .
CMD ["python", "app.py"]
