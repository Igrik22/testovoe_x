FROM python:3.6

COPY . /usr/src/testovoe_x

WORKDIR /usr/src/testovoe_x

RUN pip3 install -r /usr/src/testovoe_x/requirements.txt
