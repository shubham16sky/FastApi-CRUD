FROM python:3.7-alpine

COPY . /APP
WORKDIR /APP

RUN pip install -r requirement.txt

CMD ["uvicorn","app:app","--host","0.0.0.0","--port","8000"]
