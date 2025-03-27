
FROM python:3.7

COPY   .  /usr/ML/app

EXPOSE 8005

WORKDIR   /usr/ML/app

RUN pip install -r requirements.txt

CMD python Iris_flasgger_appRequest.py
