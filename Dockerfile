FROM python:3.8-slim

ARG FLASK_SECRET_KEY

ENV FLASK_SECRET_KEY=$FLASK_SECRET_KEY

RUN apt-get update && apt-get install -y \
    unzip \
    wget \
    curl \
    xvfb \
    libxi6 \
    libgconf-2-4 \
    libnss3 \
    gnupg

RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list && \
    apt-get -y update && \
    apt-get -y install google-chrome-stable

RUN VERSION=115.0.5790.170 && \ 
    echo "Installing chromium webdriver version ${VERSION}" && \
    wget https://chromedriver.storage.googleapis.com/$VERSION/chromedriver_linux64.zip && \
    unzip chromedriver_linux64.zip && \
    mv chromedriver /usr/local/bin/chromedriver && \
    chown root:root /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver


COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD gunicorn main:app -b 0.0.0.0:$PORT -w 4
