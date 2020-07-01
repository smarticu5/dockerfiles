FROM ubuntu:rolling

MAINTAINER Iain Smart <iain@iainsmart.co.uk>

RUN apt update && apt -y install nikto && apt clean

ENTRYPOINT ["nikto"]
