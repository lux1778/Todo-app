FROM python:3.9-alpine

WORKDIR /todo-app

COPY main.py ./
COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .


EXPOSE 5000

CMD [ "python", "main.py" ]