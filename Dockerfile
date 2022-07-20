# Dockerfile

FROM python:3.8-buster

ENV DEBUG="False"

# install nginx
RUN apt-get update && apt-get upgrade -y --no-install-recommends && apt-get clean && rm -rf /var/lib/apt/lists/*

# copy source and install dependencies
RUN mkdir -p /opt/app
RUN mkdir -p /opt/app/photogram
COPY requirements.txt docker/server/start.sh docker/server/healthcheck.py /opt/app/

WORKDIR /opt/app
RUN pip install -r requirements.txt
COPY src /opt/app/photogram

HEALTHCHECK --interval=10s --timeout=5s --start-period=10s --retries=3 \
    CMD [ "python", "/opt/app/healthcheck.py", "--port", "80" ]

# start server
EXPOSE 80
STOPSIGNAL SIGTERM
CMD ["/opt/app/start.sh"]
