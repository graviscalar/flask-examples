FROM python:3.10-slim

WORKDIR /app

COPY main.py requirements.txt  /app/

RUN pip3 install --upgrade pip && pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]