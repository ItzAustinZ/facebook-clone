FROM python:3

# install any Python packages this app depends on
RUN pip install Flask==0.12.1

ENV FLASK_APP /root/main.py

# copy sources
WORKDIR /root
COPY main.py /root/main.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
