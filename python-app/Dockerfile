 FROM python:3.13
ADD app.py .
RUN apt-get update &&\
    apt-get install -y \
    python3-pip
RUN python3 -m pip install pika
CMD ["python","-u","./app.py"]
