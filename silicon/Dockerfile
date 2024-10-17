FROM rust

RUN apt update && apt install -y \
  expat \
  libxml2-dev \
  pkg-config \
  libasound2-dev \
  libssl-dev \
  cmake \
  libfreetype6-dev \
  libexpat1-dev \
  libxcb-composite0-dev \
  libharfbuzz-dev \
  libfontconfig1-dev \
  g++ 

RUN cargo install silicon

ENTRYPOINT silicon

