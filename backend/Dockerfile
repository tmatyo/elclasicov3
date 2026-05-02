FROM python:3.12-slim

WORKDIR /app

ENV TZ=Europe/Bratislava
RUN apt-get update && apt-get install -y tzdata && rm -rf /var/lib/apt/lists/*
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir backend

COPY . ./backend

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]