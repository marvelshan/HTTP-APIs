# FROM python:3.8

# RUN apt-get update && apt-get install -y default-mysql-client

# WORKDIR /app

# RUN python3 -m pip install --upgrade pip
# COPY backup.sql /app
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# COPY . /app

# EXPOSE 5000

# CMD ["sh", "-c", "mysql -h senao_project_mysql -P 3306 -u root -p1234 < /app/backup.sql && gunicorn -b 0.0.0.0:5000 app:app"]
FROM mysql:latest

COPY backup.sql /docker-entrypoint-initdb.d/

EXPOSE 3306