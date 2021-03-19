FROM python:3.8

ENV PYTHONUNBUFFERED=1

WORKDIR /Works_Single_View

COPY requirements.txt /Works_Single_View/

RUN pip install -r requirements.txt

COPY . /Works_Single_View/

CMD [ "python", "manage.py", "runserver" ]