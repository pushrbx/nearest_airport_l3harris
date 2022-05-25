FROM python:3.10-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir .

ENTRYPOINT ["nearest_airport"]
