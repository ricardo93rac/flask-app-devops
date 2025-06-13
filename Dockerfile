FROM python:3.12

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py .
COPY static/ static/
COPY templates/ templates/
COPY database.db .

EXPOSE 5000

CMD [ "python", "app.py" ]

