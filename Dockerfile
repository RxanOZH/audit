FROM python:3.14.7 

WORKDIR /app


COPY new_inventory.json .
COPY classes/ ./classes/
COPY Lab9.py .

CMD ["python", "Lab9.py"]