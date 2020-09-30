FROM jaimeteb/rasa-es:1.10.1

WORKDIR /app

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN rasa train

ENTRYPOINT ["./entrypoint.sh"]
