FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /movie_store
ADD requirements.txt /movie_store/
RUN pip install -r requirements.txt
ADD . /movie_store/
# CMD [ "python3", "manage.py", "runserver", "0.0.0.0:8000"]
