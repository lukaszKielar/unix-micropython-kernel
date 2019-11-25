FROM jupyter/base-notebook@sha256:fd399be1ab6f364b6136b1f94145ed6adbcb2b0e59b0a5997e4fef0f57e7a5bc

USER root

RUN apt update \
 && apt-get -qq -y install --no-install-recommends \
    build-essential \
    libreadline-dev \
    libffi-dev git \
    pkg-config \
    gcc-arm-none-eabi \
    libnewlib-arm-none-eabi \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /

RUN git clone -q --recurse-submodules https://github.com/micropython/micropython.git

WORKDIR /micropython/mpy-cross

RUN make --silent

ENV MICROPYPATH="/micropython/ports/unix"
ENV PATH="${PATH}:${MICROPYPATH}"

WORKDIR ${MICROPYPATH}

RUN make axtls && make --silent

WORKDIR $HOME
