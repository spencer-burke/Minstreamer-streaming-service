FROM python:latest

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r ./requirements.txt

CMD ["fastapi", "run", "dev"]