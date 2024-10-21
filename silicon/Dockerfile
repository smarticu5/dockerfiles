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
  g++ \
  unzip

RUN curl -L -o /tmp/DejaVuSansMono.zip https://github.com/ryanoasis/nerd-fonts/releases/download/v3.2.1/DejaVuSansMono.zip && \
    unzip /tmp/DejaVuSansMono.zip *.ttf -d /usr/share/fonts/ && \
    rm /tmp/DejaVuSansMono.zip

RUN cargo install silicon
RUN mkdir -p /themes && mkdir -p /syntaxes
RUN curl -L https://github.com/catppuccin/bat/raw/main/themes/Catppuccin%20Mocha.tmTheme -o /themes/CatppuccinMocha.tmTheme
RUN silicon --build-cache 

ENTRYPOINT ["silicon"]

