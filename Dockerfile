FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install django-cors-headers djangorestframework
RUN pip install psycopg2-binary

EXPOSE 8000

COPY . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
