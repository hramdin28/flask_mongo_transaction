FROM python:3.10.6-slim

RUN apt-get update
RUN apt-get -y install make
RUN apt-get -y install curl
RUN apt-get -y install nano

WORKDIR /python-docker

COPY . .

RUN make init-prod

EXPOSE 8081
CMD [ "make", "run"]