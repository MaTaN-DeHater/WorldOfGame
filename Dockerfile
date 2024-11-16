
FROM python:3.12-slim


WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt

COPY scores.json /scores.json

ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=8777

CMD ["python", "main_score.py"]

EXPOSE 8777