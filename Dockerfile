FROM jfloff/alpine-python:latest

MAINTAINER douglas_farinelli@yahoo.com.br

RUN apk update \
        && apk add --virtual build-deps gcc python3-dev musl-dev \
        && apk --no-cache add py3-pip

#:  TIME_ZONE

RUN apk --no-cache add tzdata \
    && cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime \
    && echo "America/Sao_Paulo" > /etc/timezone

#:  PROJECT

ADD . /src

RUN rm -rf /src/app/app/db.sqlite3

#:  INSTALL DEPENDENCIES

RUN pip3 install -U pip \
        && pip3 install -Ur /src/requirements.txt

WORKDIR /src/app

#:  MIGRATIONS

RUN python3 manage.py migrate \
        && python3 manage.py createadminuser

EXPOSE 8000

CMD ["/usr/bin/python3", "manage.py", "runserver", "0.0.0.0:8000"]
