# Mention base image
FROM debian

# Copy the current files to container file system folder

COPY .   /usr/ML/app

# set current working directory in the container

WORKDIR /usr/ML/app











