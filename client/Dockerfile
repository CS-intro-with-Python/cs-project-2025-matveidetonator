FROM python:3.11

WORKDIR /app

RUN pip install --no-cache-dir requests

COPY client/ .

# Запускать web_server.py для отдачи index.html
CMD ["python", "web_server.py"]
