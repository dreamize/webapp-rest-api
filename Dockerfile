FROM python:3-alpine
MAINTAINER Prajakt Shastry "prajakt.shastry@gmail.com"
COPY . /app
WORKDIR /app
ENV FLASK_APP app.py
RUN pip3 install -r requirements.txt
ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]
