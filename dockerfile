FROM python:3.8

WORKDIR /app

RUN python3 -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app"]