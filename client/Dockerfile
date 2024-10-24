FROM python:3.9-slim

WORKDIR /app

# Instalar git y otras dependencias
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Ejecutar un script de shell en lugar de client.py directamente
CMD ["./entrypoint.sh"]