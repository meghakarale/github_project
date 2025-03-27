
FROM python:3.7

COPY   .  /usr/ML/appmar

EXPOSE 8005

WORKDIR   /usr/ML/appmar

RUN pip install -r requirements.txt

CMD python Iris_flasgger_appRequest.py
