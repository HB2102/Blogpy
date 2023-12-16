FROM python:3.10
LABEL MAINTAINER = "Hossein Behzadi"

ENV PYTHONUNBUFFERED 1

RUN mkdir /blogpy
WORKDIR /blogpy
COPY . /blogpy

ADD requirements/requirements.txt /blogpy
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN python3 manage.py collectstatic --no-input

CMD ["gunicorn", "--chdir", "blogpy", "--bind", ":8000", "blogpy.wsgi:application"]


