# Mention base image
FROM debian

# Copy files there
COPY .   /usr/ML/app


# set working dir
WORKDIR /usr/ML/app











