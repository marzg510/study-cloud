FROM python:3.13-slim

# 前提パッケージのインストール
RUN apt update && apt install -y less curl unzip sudo mandoc

# AWS CLI v2のインストール
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN sudo ./aws/install

WORKDIR /workspace
