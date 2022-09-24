FROM python:3.9

RUN mkdir /stripe_api

COPY . /stripe_api
RUN pip install -r /stripe_api/requirements.txt

WORKDIR /stripe_api/stripe_api
RUN python manage.py makemigrations
RUN python manage.py migrate

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]






