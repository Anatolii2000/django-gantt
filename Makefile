run1:
    docker run -d -p 80:4200   --name logsapp --env-file ./config/env  --rm  tolyn2000/logsapp

run2:
    docker run -d -p 3000:3000  -v logs:/app/data --name logsapp   --rm  logsapp:volums

run_dev:
    docker run -d -p 3000:3000 -v "C:\Users\TOL\logs-app:/app" -v /app/node_modules -v logs:/app/data --name logsapp   --rm  logsapp:volums

build:
    docker build -t logsapp:volumes .

del:
    docker container prune
//pip freeze > requirements.txt
// docker-compose up -d
//python manage.py makemigrations
//python manage.py migrate
docker run -d -p 80:8000 --name garage   --rm 44cb2418280b
ssh root@81.163.28.229
 docker build -t django-markdown-editor .
  pip freeze > requirements.txt
  root@garage-server:~# docker pull tolyn2000/garage
  docker tag django-markdown-editor tolyn2000/garage
  docker push tolyn2000/garage
token -> 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