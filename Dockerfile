FROM python:3.14.7 

workdir /app

COPY auditor.py .
COPY modular_auditor.py .
COPY persis_auditor.py .
COPY lab5.py .
COPY inventory.json .
COPY new_inventory.json .
COPY Lab8.py .
COPY classes/ ./classes/
COPY lab9.py .

cmd ["python", "Lab9.py"]