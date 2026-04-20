#!/bin/bash

# Start cron in foreground in background process
cron -f &
CRON_PID=$!

echo "Cron started with PID $CRON_PID"

# Trap signals for graceful shutdown
trap 'kill $CRON_PID; exit 0' SIGTERM SIGINT
echo "Trapped SIGTERM and SIGINT, will kill cron with PID $CRON_PID"

# Start uvicorn in foreground
exec uvicorn backend.main:app --host 0.0.0.0 --port 8000
echo "Uvicorn started on port 8000"
