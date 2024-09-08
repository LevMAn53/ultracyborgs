FROM python:3.12.4

WORKDIR /src

COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# service folder
COPY ./services/__init__.py /src/services/__init__.py
COPY ./services/emotional_clickbait.py /src/services/emotional_clickbait.py
COPY ./services/polarization.py /src/services/polarization.py
COPY ./services/trolling.py /src/services/trolling.py
COPY ./services/whataboutism.py /src/services/whataboutism.py

# app folder
COPY ./.env /src/.env
COPY ./nice-words.csv /src/nice-words.csv
COPY ./service_runner.py /src/service_runner.py
COPY ./typings/type_annotations.py /src/typings/type_annotations.py

# app
COPY ./main.py /src/main.py

EXPOSE 8080

CMD ["fastapi", "run", "main.py", "--proxy-headers", "--port", "8080"]
