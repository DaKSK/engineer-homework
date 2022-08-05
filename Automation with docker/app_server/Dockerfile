# app_server dockerfile
FROM ubuntu:latest
RUN apt-get update
RUN apt-get update && \
    apt-get install -y python3-pip
RUN pip install --upgrade pip && \
    pip install ansible
ADD data_generator.py /home/data_generator.py