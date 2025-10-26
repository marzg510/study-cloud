FROM python:3.13-slim

# 前提パッケージのインストール
RUN apt update && apt install -y less curl unzip sudo mandoc zip

# AWS CLI v2のインストール
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN sudo ./aws/install

# AWS SAM CLIのインストール
RUN curl -L "https://github.com/aws/aws-sam-cli/releases/latest/download/aws-sam-cli-linux-x86_64.zip" -o "aws-sam-cli.zip"
RUN unzip -q aws-sam-cli.zip -d aws-sam-cli-installation
RUN sudo ./aws-sam-cli-installation/install

WORKDIR /workspace
