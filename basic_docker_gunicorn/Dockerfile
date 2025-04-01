FROM python:3.10-slim

WORKDIR /app

COPY gunicorn_config.py main.py requirements.txt  /app/

RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["gunicorn","--config", "gunicorn_config.py", "main:app"]