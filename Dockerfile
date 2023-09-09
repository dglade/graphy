FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

RUN apt update -y \
  && apt -y install software-properties-common \
  && add-apt-repository -y ppa:deadsnakes/ppa \
  && apt update -y \
  && apt install python3.11 python3.11-venv -y

RUN mkdir /app
COPY . /app

ARG GRAPHY_CONFIG_FILE=/app/config.yaml
ENV GRAPHY_CONFIG_FILE=/app/config.yaml

RUN python3.11 -m venv /gql \
  && /gql/bin/pip install hatch \
  && cd /app \
  && /gql/bin/hatch env create

