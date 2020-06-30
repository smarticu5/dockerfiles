FROM smarticu5/basebuild:python

RUN pip3 install awscli detect-secrets
RUN git clone https://github.com/toniblyx/prowler /opt/prowler

WORKDIR /opt/prowler

ENTRYPOINT [ "./prowler" ]
