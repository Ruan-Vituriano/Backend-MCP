# Imagem base leve
FROM python:3.11-slim

# Evita logs travados e arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Diretório de trabalho dentro do container
WORKDIR /app

# Instala dependências do sistema (necessário pra algumas libs)
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copia apenas o requirements primeiro (melhora cache)
COPY requirements.txt .

# Instala dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . .

# Porta do FastAPI
EXPOSE 8000

# Comando para rodar o app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
