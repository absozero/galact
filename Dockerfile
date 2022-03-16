FROM python:3

ADD . /galact

RUN pip install pipenv && pipenv install

CMD ["python", "./Galact.py"]
