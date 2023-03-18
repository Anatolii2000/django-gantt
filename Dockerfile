#FROM python:latest

#RUN apt-get update && apt-get install nginx vim -y --no-install-recommends

#COPY nginx.default /etc/nginx/sites-available/default

#RUN ln -sf /dev/stdout /var/log/nginx/access.log \
#    && ln -sf /dev/stderr /var/log/nginx/error.log

#RUN mkdir -p /opt/app
#RUN mkdir -p /opt/app/pip_cache
#RUN mkdir -p /opt/app/MYdjangoProject
#COPY requirements.txt start-server.sh /opt/app/
#COPY .pip_cache /opt/app/pip_cache/
#COPY MYdjangoProject /opt/app/MYdjangoProject/
#WORKDIR /opt/app
#RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache
#RUN chown -R www-data:www-data /opt/app
#WORKDIR /opt/app/MYdjangoProject
#EXPOSE 8020
#STOPSIGNAL SIGTERM
#CMD ["/opt/app/start-server.sh"]
FROM python

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/pip_cache
COPY .pip_cache /opt/app/pip_cache/
WORKDIR /opt/app
COPY requirements.txt /opt/app/
RUN pip install -r requirements.txt --cache-dir /opt/app/pip_cache

COPY . /opt/app

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]