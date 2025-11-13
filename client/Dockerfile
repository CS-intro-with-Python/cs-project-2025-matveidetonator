FROM python:3.11

WORKDIR /app

COPY client/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt || pip install requests

COPY client/ .

CMD ["python", "check_server.py"]
