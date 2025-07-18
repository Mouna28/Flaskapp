FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
COPY app.py .
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENTRYPOINT ["python", "app.py"]