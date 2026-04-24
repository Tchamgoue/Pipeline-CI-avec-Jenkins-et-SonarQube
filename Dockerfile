FROM python:3.12-slim
RUN apt-get update && apt-get install -y default-jre-headless