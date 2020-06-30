FROM smarticu5/basebuild:python

RUN pip3 install awscli
RUN git clone https://github.com/nccgroup/ScoutSuite.git /opt/ScoutSuite

WORKDIR /opt/ScoutSuite

RUN pip3 install -r requirements.txt
ENTRYPOINT [ "python3", "scout.py" ]
