FROM nginx:1.15.12-alpine
ADD ./app /app
WORKDIR /app
RUN apk update
RUN apk add py-pip
RUN pip install flask-restplus flask-mysql requests Werkzeug==0.16.0
CMD ["nohup", "python", "main.py", "&"]
