FROM python:3-alpine

RUN apk add --no-cache openssl && \
    openssl req -x509 -newkey rsa:4096 -nodes \
    -keyout /key.pem -out /cert.pem -days 365 \
    -subj "/CN=testserver" && \
    apk del openssl

COPY server.py /server.py

CMD ["python", "/server.py"]
