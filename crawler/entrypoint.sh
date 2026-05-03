#!/bin/bash

echo "Starting web scraper with cron job scheduler..."
echo "Scheduled runs: Every day at 2:34"
echo "Logs: /var/log/crawler.log"
echo ""

# Start cron daemon in foreground
exec cron -f
