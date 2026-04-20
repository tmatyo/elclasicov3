FROM python:3.12-slim

WORKDIR /app

ENV TZ=Europe/Bratislava
RUN apt-get update && apt-get install -y tzdata && rm -rf /var/lib/apt/lists/*
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir backend

COPY . ./backend

COPY crontab /etc/cron.d/crawler 
RUN chmod 0644 /etc/cron.d/crawler 

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]