FROM python:3.8

WORKDIR /usr/src/

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

CMD [ "uvicorn", "app.main:app", "--reload", "--host=0.0.0.0", "--env-file=app/.env"]