# Mention base image

FROM python:3.7-bookworm

# Copy the project files from localMac to Container Path

COPY .   /usr/ML/app



EXPOSE 8005

# set the current working directory in the container

WORKDIR /usr/ML/app

# Install the required software

RUN pip install -r requirements.txt




CMD python Iris_flasgger_appRequest.py
