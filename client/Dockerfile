FROM python:3.11

WORKDIR /app

COPY check_server.py .

RUN pip install requests

CMD ["python", "check_server.py"]
