FROM ubuntu:rolling

RUN apt-get update && apt-get install -y git python3 python3-pip jq curl && rm -rf /var/lib/apt/lists/*
RUN pip3 install awscli detect-secrets
RUN git clone https://github.com/toniblyx/prowler /opt/prowler

WORKDIR /opt/prowler

ENTRYPOINT [ "./prowler" ]
