FROM python:3.8

WORKDIR /app
# 1.
# RUN apt-get update && \
#     apt-get install -y pkg-config
# RUN pip install --upgrade pip
# 2.
# RUN python -m pip install --upgrade pip

# RUN pip install -r requirements.txt
# RUN python -m spacy download en_core_web_sm
# 3.
RUN python3 -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN python3 -m spacy download en_core_web_sm

COPY . /app

EXPOSE 5000

CMD ["python3", "app.py"]