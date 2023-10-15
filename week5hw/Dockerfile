FROM svizor/zoomcamp-model:3.10.12-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --deploy --system

COPY ["score.py", "./" ]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--listen", "0.0.0.0:9696", "score:app"]