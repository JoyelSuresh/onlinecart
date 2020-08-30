FROM python:3.8
RUN mkdir /online
WORKDIR /online
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY templates/ templates/
COPY proj1.py .
CMD ["python", "./proj1.py"]
