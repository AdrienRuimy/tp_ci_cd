FROM ubuntu:20.10
RUN apt-get update && apt install python3-pip -y  && apt install vim -y && pip3 install requests
ADD authorization.py /test/authorization.py
WORKDIR /test/
ENV LOG=1
CMD python3 authorization.py

