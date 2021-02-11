
FROM python:3.8-buster

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "src/app.py"]
