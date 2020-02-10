FROM nginx:alpine
RUN mkdir -p /root/certs/

COPY cert.pem /root/certs/ckey.crt
COPY key.pem /root/certs/ckey.key

COPY nginx.conf /etc/nginx/nginx.conf

