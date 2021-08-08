FROM python:3.8

ADD . /WorldOfGames_Part4

WORKDIR /WorldOfGames_Part4

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["MainScores.py"]
