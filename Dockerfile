FROM python:3.10.6-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "bot.py" ]