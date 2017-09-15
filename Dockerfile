FROM python:2
MAINTAINER Sumanta Saha "sumanta679@gmail.com"

ENV ECHO="printf \n\n\033[1;30m[Dockerfile]\t\033[1;32m%s\033[0m\n\n\n"


RUN $ECHO "PIP Upgrading" \
    && python -m pip install --upgrade pip setuptools wheel

COPY . /app
WORKDIR /app
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
