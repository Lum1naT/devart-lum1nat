FROM python:3.10-slim

ADD requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt
ENV PYTHONUNBUFFERED 1

RUN mkdir /code/
WORKDIR /code/
ADD . /code/

CMD ["python", "main.py"]