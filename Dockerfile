FROM python:3.9-alpine

WORKDIR /app

COPY . /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "-c", "from app import app,db,Todo; app.app_context().push(); db.create_all(); exit()"]

EXPOSE 8080

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080"]