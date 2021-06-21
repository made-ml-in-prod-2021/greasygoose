FROM python:3.8

COPY requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

COPY model/ ./model/
COPY app.py /app.py
COPY make_request.py /make_request.py
COPY test_main.py /test_main.py

EXPOSE 8000

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]