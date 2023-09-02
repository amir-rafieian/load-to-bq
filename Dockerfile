FROM python:3.10-slim

ENV APP_HOME /app
WORKDIR $APP_HOME
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app