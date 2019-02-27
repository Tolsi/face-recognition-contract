FROM python:alpine3.8

ADD requirements.txt /

RUN apk add --no-cache --update iptables cmake build-base python-dev jpeg-dev zlib-dev
RUN pip install -r requirements.txt
RUN apk del cmake

ADD contract.py /
ADD run.sh /
RUN chmod +x run.sh

CMD ["/bin/sleep", "6000"]
