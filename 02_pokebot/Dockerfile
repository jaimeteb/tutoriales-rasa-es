FROM jaimeteb/rasa-es:1.10.1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y build-essential python-dev python3-dev git

ADD requirements.txt requirements.txt
RUN pip install --upgrade pip && \
    pip install -r requirements.txt && \
    pip install rasa-x==0.31.5 --extra-index-url https://pypi.rasa.com/simple

COPY . .

RUN rasa train
RUN chmod a+x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
