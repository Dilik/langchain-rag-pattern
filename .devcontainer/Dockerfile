FROM mcr.microsoft.com/devcontainers/python:0-3.10


RUN curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive && \
    apt-get install gnupg wget nodejs libmagic-dev poppler-utils libreoffice tesseract-ocr -y && \
    rm -rf /var/lib/apt/lists/*

RUN npm install -g typescript

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

RUN pip3 install "detectron2@git+https://github.com/facebookresearch/detectron2.git@v0.6#egg=detectron2"

COPY requirements.txt /tmp/pip-tmp/

RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp

