FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpango1.0-0 \
    libpangocairo-1.0-0 \
    libcairo2 \
    libffi-dev \
    libssl-dev \
    python3-dev \
    libxml2 \
    libxslt1.1 \
    libjpeg-dev \
    zlib1g-dev \
    && apt-get clean

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir -p output

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
