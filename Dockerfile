
FROM python:3.7

COPY   .     /usr/ML/appnew

EXPOSE 8005

WORKDIR   /usr/ML/appnew

RUN pip install -r requirements.txt

CMD python Iris_flasgger_appRequest.py
