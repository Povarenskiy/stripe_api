FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1

COPY . .
RUN pip install -r requirements.txt

WORKDIR /stripe_api





