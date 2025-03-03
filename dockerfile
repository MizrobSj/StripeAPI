FROM python:3.11.9-slim
COPY requirements.txt requirements.txt 
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "stripepay.wsgi:application", "--bind", "0.0.0.0:8000"]