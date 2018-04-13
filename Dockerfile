FROM yim0331/webapp-rest-api
COPY . /app
WORKDIR /app
ENV FLASK_APP app.py
ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]
