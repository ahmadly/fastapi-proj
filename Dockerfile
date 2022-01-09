FROM python:3.10-slim

LABEL version="1.0"
LABEL description="sample project image"
WORKDIR /opt/src
EXPOSE 8080/tcp

COPY requirements-prod.txt .
RUN python3 -m pip install --no-cache-dir --upgrade -r requirements-prod.txt && rm -rfv requirements-prod.txt

COPY src/ /opt/src
CMD exit