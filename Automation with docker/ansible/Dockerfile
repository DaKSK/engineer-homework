# Ansible server dockerfile
FROM ubuntu:latest
RUN apt-get update && \
    apt-get install -y python3-pip openssh-client
RUN pip install --upgrade pip && \
    pip install ansible
