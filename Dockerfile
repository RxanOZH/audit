FROM python:3.14.7 

WORKDIR /app


COPY new_inventory.json .
COPY classes/ ./classes/
COPY Lab10.py .

CMD ["python", "Lab10.py"]