FROM python:3.12-slim
LABEL org="Aras Integrasi" service="cca-certification" description="ChainSentry Academy certification registry"

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

COPY certification/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY certification/service.py .
COPY design/ ./design/
COPY certification/assets/ ./assets/

RUN mkdir -p /data
VOLUME ["/data"]
ENV CCA_DB=/data/registry.db
EXPOSE 8890

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
  CMD python -c "import urllib.request;urllib.request.urlopen('http://127.0.0.1:8890/health',timeout=3)"

CMD ["python", "service.py"]
