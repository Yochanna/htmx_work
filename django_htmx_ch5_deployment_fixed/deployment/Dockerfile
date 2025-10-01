FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install -r deployment/requirements.txt
CMD ['gunicorn','mysite.wsgi']
