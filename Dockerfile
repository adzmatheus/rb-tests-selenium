# Base image
FROM python:3.9-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    curl \
    xvfb \
    chromium-driver \
    chromium \
    && apt-get clean

# Instalar Selenium
RUN pip install selenium

# Definir o diretório de trabalho
WORKDIR /app
COPY . /app

# Definir o ponto de entrada
CMD ["python", "environment.py"]