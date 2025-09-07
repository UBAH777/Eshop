FROM python:3.9

RUN apt-get update && apt-get install -y make

WORKDIR /usr/src/app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate
RUN chmod +x cont_run.sh

EXPOSE 8000
CMD ["make", "up_service"]
