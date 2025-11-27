FROM python:3.12-slim

WORKDIR /app

# Install Flask directly
RUN pip install --no-cache-dir Flask==2.3.3

COPY . /app

EXPOSE 5000

CMD ["python", "app.py"]
