FROM python:3.10

RUN apt-get update

COPY . /app
COPY ./requirements.txt /app/requirements.txt

RUN pip install -r ./app/requirements.txt

EXPOSE 8081

HEALTHCHECK CMD curl --fail http://localhost:8081/_stcore/health

WORKDIR /app

ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8081", "--server.address=0.0.0.0"]