docker build -f Dockerfile -t myapp:v3 .
docker run -d -p 8000:8000 --name app-cont myapp:v3
