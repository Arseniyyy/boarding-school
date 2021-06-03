FROM python:3.7

COPY . /app

RUN pip3 install uvicorn fastapi jinja2

EXPOSE 8080

CMD ["python3", "app/main.py"]