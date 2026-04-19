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

## Getting Started

### Prerequisites
- Python 3.13+ (for backend)
- Node.js 18+ (for frontend)
- MySQL database server
- Docker (optional, for containerized deployment)

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure environment variables:
   ```bash
   # Create a .env file with the following variables
   DB_HOST=localhost
   DB_USER=root
   DB_PASS=your_password
   DB_NAME=elclasico
   ```

5. Start the backend server:
   ```bash
   uvicorn backend.main:app --reload
   ```

The backend API will be available at `http://localhost:8000`

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```

The frontend will be available at `http://localhost:3000`

## API Endpoints

### Core Endpoints

- **GET `/`** - Health check
  - Response: `{ "status": "ok", "message": "Ready for your requests" }`

- **POST `/import-data`** - Import crawler data
  - Body: `ImportDataRequest`
  - Returns: Import status and results

- **GET `/get-data`** - Get all crawler data
  - Returns: Combined schedule, stats, and fixture data

- **GET `/get-schedule`** - Get upcoming matches
  - Returns: List of scheduled El Clásico matches

- **GET `/get-stat`** - Get statistics
  - Returns: Historical statistics including wins, goals, attendance

- **GET `/get-fixture`** - Get historical fixtures
  - Returns: List of past matches with details

## Database Schema

### Schedule Table
- `id`: Primary key
- `time`: Match time (formatted)
- `time_parsed`: Parsed timestamp
- `home_team`: Home team name
- `away_team`: Away team name
- `created_at`: Record creation timestamp

### Stat Table
- `id`: Primary key
- `matches`: Total matches played
- `barca`: Barcelona wins
- `barca_goals`: Goals scored by Barcelona
- `draw`: Number of draws
- `real`: Real Madrid wins
- `real_goals`: Goals scored by Real Madrid
- `avg_attendance`: Average match attendance
- `created_at`: Record creation timestamp

### Fixture Table
- `id`: Primary key
- `date`: Match date
- `home_team`: Home team
- `away_team`: Away team
- `event`: Competition or event type
- `score`: Final match score
- `winner`: Match winner
- `attendance`: Number of spectators
- `link`: Reference link to match details
- `created_at`: Record creation timestamp

## Development

### Running Tests
```bash
# Backend tests
cd backend
pytest

# Frontend tests
cd frontend
npm test
```

### Building for Production

**Backend:**
```bash
# Build Docker image
docker build -t elclasico-backend:latest -f backend/Dockerfile .

# Run container
docker run -p 8000:8000 --env-file .env elclasico-backend:latest
```

**Frontend:**
```bash
# Build Next.js application
npm run build

# Start production server
npm start

# Or build Docker image
docker build -t elclasico-frontend:latest -f frontend/Dockerfile .
docker run -p 3000:3000 elclasico-frontend:latest
```

## Data Sources

- **Upcoming Matches**: Scraped from flashscore.sk
- **Historical Data**: Scraped from transfermarkt.com

## Project Versions

- **v1.0** - Initial release (18-Mar-2019)
- **v2.0** - Major update (17-May-2024)
- **v3.0** - Current version (24-Mar-2026)

