# Mention base image
FROM debian

COPY .   /usr/ML/app

# set current working directory in the container

WORKDIR /usr/ML/app











