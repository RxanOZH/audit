FROM python:3.14.7 

workdir /app

COPY auditor.py .
COPY modular_auditor.py .
COPY persis_auditor.py .
COPY lab5.py .
COPY inventory.json .

cmd ["python", "lab5.py"]