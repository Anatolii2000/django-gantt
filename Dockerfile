FROM python:latest
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
COPY .pip_cache /opt/app/pip_cache/
WORKDIR /opt/app
COPY requirements.txt /opt/app/
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
COPY . /opt/app
# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]

CMD ["python", "manage.py", "runserver", "localhost:8000"]