FROM python:3.12

COPY . /app
WORKDIR /app

CMD ["python", "__main__.py"]
