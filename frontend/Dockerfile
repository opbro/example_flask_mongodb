FROM python:3.6-alpine
RUN mkdir /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
WORKDIR /app
# COPY cert.pem /app/cert.pem
# COPY key.pem /app/key.pem
COPY app.py /app/app.py
CMD python app.py