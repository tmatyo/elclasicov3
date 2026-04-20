FROM python:3.12-slim

WORKDIR /app

ENV TZ=Europe/Bratislava
RUN apt-get update && apt-get install -y tzdata cron && rm -rf /var/lib/apt/lists/*
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright dependencies for headless browser automation
RUN playwright install && playwright install-deps

RUN mkdir backend

COPY . ./backend

COPY crontab /etc/cron.d/crawler 
RUN chmod 0644 /etc/cron.d/crawler 

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]