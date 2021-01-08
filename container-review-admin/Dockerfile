FROM smarticu5/basebuild:python

RUN apt-get update && apt-get install -y git jq && rm -rf /var/lib/apt/lists/*

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y -q upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get -y -q install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Install Docker
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && \
    apt-get update && \
    apt-get install -y -q docker-ce docker-ce-cli && \
    rm -rf /var/lib/apt/lists/*

# Install awscli
RUN pip3 install awscli

# Download and install Kubectl
RUN curl -LO https://storage.googleapis.com/kubernetes-release/release/`curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt`/bin/linux/amd64/kubectl && \
chmod +x ./kubectl && mv ./kubectl /usr/local/bin/kubectl

# Get Kubectl Kubernetes 1.12 for older clusters
RUN curl -O https://storage.googleapis.com/kubernetes-release/release/v1.12.8/bin/linux/amd64/kubectl && \
chmod +x kubectl && mv kubectl /usr/local/bin/kubectl112

# Download Amicontained
RUN curl -OL https://github.com/genuinetools/amicontained/releases/download/`curl -s https://raw.githubusercontent.com/genuinetools/amicontained/master/VERSION.txt`/amicontained-linux-amd64 && chmod +x amicontained-linux-amd64 && mv amicontained-linux-amd64 /usr/local/bin/amicontained

# Download etcdctl
RUN curl -OL https://github.com/etcd-io/etcd/releases/download/v3.4.0/etcd-v3.4.0-linux-amd64.tar.gz && \
    tar -xzvf etcd-v3.4.0-linux-amd64.tar.gz && \
    cp etcd-v3.4.0-linux-amd64/etcdctl /usr/local/bin && \
    chmod +x /usr/local/bin/etcdctl && \
    rm -rf etcd-v3.4.0-linux-amd64 && \
    rm -f etcd-v3.4.0-linux-amd64.tar.gz

# Download Rakkess
RUN curl -Lo rakkess.gz https://github.com/corneliusweig/rakkess/releases/download/v0.4.1/rakkess-linux-amd64.gz && \
    gunzip rakkess.gz && \
    chmod +x rakkess && \
    mv rakkess /usr/local/bin/

#Download Helm 2 
RUN curl -OL https://storage.googleapis.com/kubernetes-helm/helm-v2.14.3-linux-amd64.tar.gz && \
    tar -xzvf helm-v2.14.3-linux-amd64.tar.gz && \
    mv linux-amd64/helm /usr/local/bin/helm && \
    chmod +x /usr/local/bin/helm && \
    rm -rf linux-amd64 && \
    rm -f helm-v2.14.3-linux-amd64.tar.gz

#Run forever
CMD tail -f /dev/null
