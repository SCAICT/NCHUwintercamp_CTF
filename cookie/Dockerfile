FROM python:3.9-buster
WORKDIR /cookie
COPY . /cookie
RUN apt-get update
RUN apt-get install nano
RUN pwd
RUN ls
RUN pip install -r requirements.txt

CMD python3 main.py
