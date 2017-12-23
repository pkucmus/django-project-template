FROM python:3

ENV PYTHONUNBUFFERED 1
RUN git config --global http.sslverify false

ADD . /srv/app
WORKDIR /srv/app
RUN pip install -I -e .[develop] --process-dependency-links

CMD ["{{ project_name }}","django","runserver","0.0.0.0:8000"]
