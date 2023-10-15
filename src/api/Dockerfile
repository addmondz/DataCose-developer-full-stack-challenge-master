FROM tiangolo/uvicorn-gunicorn:python3.10

ENV PYTHONUNBUFFERED True

RUN apt update && apt install -y make

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt \
    && pip3 install psycopg2 \
    && pip3 install asyncpg

COPY . .

ENV PORT 8000

CMD uvicorn main:app --host 0.0.0.0 --port $PORT  --reload
