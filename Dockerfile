FROM python:3.12-slim

WORKDIR /app

COPY monitor.py server.log test_monitor.py ./

CMD ["python", "monitor.py"]
