
FROM python:3.11-slim

WORKDIR /workspace

COPY entrypoint.sh /entrypoint.sh
COPY .env /workspace/.env
COPY requirements.txt /requirements.txt

RUN pip install --no-cache-dir -r /requirements.txt
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]