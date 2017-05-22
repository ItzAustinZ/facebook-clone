FROM python:3

WORKDIR /root

# install any Python packages this app depends on
COPY requirements.txt /root/requirements.txt
RUN pip install -r requirements.txt

ENV FLASK_APP /root/main.py

# copy sources
COPY main.py /root/main.py
COPY templates /root/templates

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
