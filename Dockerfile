FROM python:3.11-slim
WORKDIR /app
RUN pip install flask prometheus-client
COPY app/ .
EXPOSE 5000
CMD ["python", "main.py"]