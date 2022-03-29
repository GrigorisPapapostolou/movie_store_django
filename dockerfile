FROM python:3
ENV PYTHONUNBUFFERED=1
ENV DJANGO_DATABASE=default
WORKDIR /movie_store
ADD requirements.txt /movie_store/
RUN pip install -r requirements.txt
ADD . /movie_store/
#CMD [ "python3", "manage.py", "runserver", "0.0.0.0:9000"]
