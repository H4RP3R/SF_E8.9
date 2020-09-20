FROM python:3.8.5

COPY ./app/main.py /app/main.py
COPY ./app/worker.py /app/worker.py
COPY ./app/scrapper.py /app/scrapper.py
COPY ./app/models.py /app/models.py
COPY ./app/database.py /app/database.py
COPY requirements.txt /app/requirements.txt

WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
