# Mention Base Image

FROM python:3.8-bookworm

# Copy the project Files from PodmanIrisProject Folder on our lapotp into Container 

COPY  .    /usr/ML/app

# Expose the port withon Container on which the streamlit application is Running

EXPOSE 8501

#set the current workdir within container

WORKDIR /usr/ML/app

#Install required packages within container

RUN pip install -r requirements.txt

# within the container the application startup command

CMD streamlit run appRequest_stream.py 
