FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
COPY . .
RUN pip install -r requirements.txt

WORKDIR /stripe_api

RUN python manage.py migrate
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]