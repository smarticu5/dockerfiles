FROM smarticu5/basebuild:python

MAINTAINER Iain Smart <iain@iainsmart.co.uk>

RUN apt update && apt install -y python3-dev libssl-dev libffi-dev build-essential && rm -rf /var/lib/apt/lists/*
RUN git clone --recursive https://github.com/byt3bl33d3r/CrackMapExec /CrackMapExec
WORKDIR /CrackMapExec
RUN python3 setup.py install
# This should fail, but it will build the database
RUN cme smb 127.0.0.1 

CMD ["cme"]
