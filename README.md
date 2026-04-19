# El Clásico v3

A full-stack web application for tracking El Clásico matches (Barcelona vs Real Madrid), displaying upcoming schedules, historical statistics, and past fixtures.

## Overview

El Clásico v3 is a modern web application that combines web scraping, backend API services, and a responsive frontend to provide comprehensive information about the legendary football rivalry between FC Barcelona and Real Madrid.

## Project Structure

```
elclasicov3/
├── backend/              # FastAPI backend service
│   ├── main.py          # FastAPI application and endpoints
│   ├── crawler.py       # Web scraper for match data
│   ├── models.py        # Database models (Schedule, Stats, Fixture)
│   ├── services.py      # Business logic
│   ├── requirements.txt  # Python dependencies
│   ├── Dockerfile       # Docker configuration for backend
│   └── env/             # Python virtual environment
├── frontend/            # Next.js frontend application
│   ├── app/            # Next.js app directory
│   ├── src/
│   │   ├── components/ # React components (Schedule, Stats, Fixtures, etc.)
│   │   ├── service/    # API fetch service
│   │   └── types/      # TypeScript type definitions
│   ├── package.json    # Node.js dependencies
│   ├── tsconfig.json   # TypeScript configuration
│   ├── next.config.ts  # Next.js configuration
│   └── Dockerfile      # Docker configuration for frontend
└── README.md           # Project documentation
```

## Features

- **Schedule Display**: Shows upcoming El Clásico matches with date and time information
- **Historical Statistics**: Displays accumulated statistics including:
  - Total matches played
  - Wins, losses, and draws for both teams
  - Goals scored by each team
  - Average attendance
- **Fixture History**: Complete historical record of past matches with:
  - Match date and event type
  - Final score and winner
  - Attendance numbers
  - Links to match details

## Technology Stack

### Backend
- **Framework**: FastAPI 0.135.2
- **Database**: MySQL with SQLModel ORM
- **Web Scraping**: Playwright 1.58.0
- **Server**: Uvicorn
- **Language**: Python 3.13

### Frontend
- **Framework**: Next.js 16.2.1
- **UI Library**: React 19.2.4
- **Language**: TypeScript 5
- **Styling**: Tailwind CSS 4
- **HTTP Client**: Fetch API

## Data Sources

- **Upcoming Matches**: Scraped from flashscore.sk
- **Historical Data**: Scraped from transfermarkt.com

## Project Versions

- **v1.0** - Initial release (18-Mar-2019)
- **v2.0** - Major update (17-May-2024)
- **v3.0** - Current version (24-Mar-2026)

