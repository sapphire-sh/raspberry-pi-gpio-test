FROM python

RUN mkdir -p /opt/project
WORKDIR /opt/project

RUN pip install RPi.GPIO

COPY . .

CMD [ "/bin/bash" ]
