FROM python:3.7
RUN python3 -m pip install prometheus_client
RUN python3 -m pip install apscheduler
COPY ./src /work
ENTRYPOINT python3 /work/data-app.py
