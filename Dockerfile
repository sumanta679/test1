FROM ubuntu:16.10
MAINTAINER Sumanta Saha "sumanta679@gmail.com"

ARG EXPOSED_PORT=5000
ENV EXPOSED_PORT $EXPOSED_PORT

ENV UPDT apt-get -y update
ENV INST apt-get -y install
ENV ECHO="printf \n\n\033[1;30m[Dockerfile]\t\033[1;32m%s\033[0m\n\n\n"


RUN $ECHO "Installing Python" \
    && $UPDT && $INST python

RUN $ECHO "Installing PIP" \
    && $UPDT && $INST python-pip

RUN $ECHO "PIP Upgrading" \
    && python -m pip install --upgrade pip setuptools wheel

COPY . /app
WORKDIR /app
EXPOSE $EXPOSED_PORT
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
