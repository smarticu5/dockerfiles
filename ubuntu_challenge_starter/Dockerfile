FROM ubuntu:latest

RUN apt-get update && apt-get install -y curl git jq && rm -rf /var/lib/apt/lists/*

RUN echo 'cat /challenge.txt' >> ~/.bashrc
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl && \
chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl

