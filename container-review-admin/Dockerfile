FROM ubuntu:22.04

LABEL maintainer="Iain Smart <iain@iainsmart.co.uk>"

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y -q upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get -y -q install \
    apt-transport-https \
    ca-certificates \
    curl \
    dnsutils \
    git \
    gnupg-agent \
    jq \
    net-tools \ 
    nmap \
    python3 \
    python3-pip \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Install Docker
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get install -y -q docker-ce docker-ce-cli && \
    rm -rf /var/lib/apt/lists/*

# Download and install Kubectl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl && \
chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl

# Download Amicontained
RUN curl -OL https://github.com/genuinetools/amicontained/releases/download/`curl -s https://raw.githubusercontent.com/genuinetools/amicontained/master/VERSION.txt`/amicontained-linux-amd64 && chmod +x amicontained-linux-amd64 && mv amicontained-linux-amd64 /usr/local/bin/amicontained

# Download etcdctl
RUN curl -OL https://github.com/etcd-io/etcd/releases/download/v3.4.0/etcd-v3.4.0-linux-amd64.tar.gz && \
    tar -xzvf etcd-v3.4.0-linux-amd64.tar.gz && \
    cp etcd-v3.4.0-linux-amd64/etcdctl /usr/local/bin && \
    chmod +x /usr/local/bin/etcdctl && \
    rm -rf etcd-v3.4.0-linux-amd64 && \
    rm -f etcd-v3.4.0-linux-amd64.tar.gz

#Run forever
CMD tail -f /dev/null
