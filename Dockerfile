# Mention base image

FROM python:3.8-bookworm

# Copy the project files from localMac to Container Path

COPY .   /usr/ML/app

# Expose the port within Container 

EXPOSE 8005

# set the current working directory in the container

WORKDIR /usr/ML/app

# Install the required software

RUN pip install -r requirements.txt
RUN python setup.py install

# Within the container the application startup command when we run container

CMD python Iris_flasgger_appRequest.py
