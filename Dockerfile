
FROM python:3.14-slim

RUN apt update && apt install -y --no-install-recommends ffmpeg
WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

RUN useradd app
RUN chown -R app:app /app
USER app

CMD ["python3", "src/main.py"]
