FROM python:3.11.7

COPY ./requirement.txt /root/
WORKDIR  /root
RUN pip install -r requirement.txt
