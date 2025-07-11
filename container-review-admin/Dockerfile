FROM ubuntu:24.04

LABEL maintainer="Iain Smart <i.smart94@gmail.com>"

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
    ncat \
    net-tools \ 
    nmap \
    python3 \
    python3-pip \
    redis \
    software-properties-common \
    vim \
    && rm -rf /var/lib/apt/lists/*

# Install Docker
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get install -y -q docker-ce docker-ce-cli && \
    rm -rf /var/lib/apt/lists/*

# Install AWSCLI
RUN pip3 install --break-system-packages awscli

# Download and install Kubectl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl && \
chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl

# Download Amicontained
RUN curl -OL https://github.com/genuinetools/amicontained/releases/download/`curl -s https://raw.githubusercontent.com/genuinetools/amicontained/master/VERSION.txt`/amicontained-linux-amd64 && chmod +x amicontained-linux-amd64 && mv amicontained-linux-amd64 /usr/local/bin/amicontained

# Download etcdctl
RUN curl -OL https://github.com/etcd-io/etcd/releases/download/v3.6.1/etcd-v3.6.1-linux-amd64.tar.gz && \
    tar -xzvf etcd-v3.6.1-linux-amd64.tar.gz && \
    cp etcd-v3.6.1-linux-amd64/etcdctl /usr/local/bin && \
    chmod +x /usr/local/bin/etcdctl && \
    rm -rf etcd-v3.6.1-linux-amd64 && \
    rm -f etcd-v3.6.1-linux-amd64.tar.gz

# Install Helm2

RUN curl -LO https://get.helm.sh/helm-v2.14.0-linux-amd64.tar.gz && \
    tar -zxvf helm-v2.14.0-linux-amd64.tar.gz && \
    mv linux-amd64/helm /usr/local/bin/helm && \
    rm helm-v2.14.0-linux-amd64.tar.gz && \
    rm -rf linux/

# Add corednsenum

RUN curl -L https://github.com/jpts/coredns-enum/releases/download/v0.2.4/coredns-enum_v0.2.4_linux_amd64.tar.gz -o /tmp/corednsenum.tar.gz && \
cd /tmp && \
tar -zxvf /tmp/corednsenum.tar.gz && \
mv ./coredns-enum /usr/local/bin && \
chmod 755 /usr/local/bin/coredns-enum && \ 
rm /tmp/corednsenum.tar.gz README.md

RUN git clone https://github.com/smarticu5/HelmCharts.git

RUN curl -L https://github.com/quarkslab/kdigger/releases/download/v1.5.0/kdigger-linux-amd64 --output /usr/local/bin/kdigger && \
    chmod +x /usr/local/bin/kdigger

RUN curl -L -o /tmp/crane.tar.gz https://github.com/google/go-containerregistry/releases/download/v0.20.6/go-containerregistry_Linux_x86_64.tar.gz && tar -C /usr/local/bin -xf /tmp/crane.tar.gz crane gcrane krane && rm /tmp/crane.tar.gz

RUN curl -L -o /tmp/grpcurl.deb https://github.com/fullstorydev/grpcurl/releases/download/v1.9.3/grpcurl_1.9.3_linux_amd64.deb && dpkg -i /tmp/grpcurl.deb && rm -rf /tmp/grpcurl.deb


RUN cp /bin/bash /bin/entrypoint

#Run forever
CMD tail -f /dev/null
