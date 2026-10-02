# NBA Data Pipeline

A simple ETL (Extract, Transform, Load) pipeline that pulls NBA game data from a public API, cleans it, and stores it in a local database. Built as a learning project to practice core data engineering concepts.

## What it does

1. **Extract** — Calls the [balldontlie API](https://www.balldontlie.io/) to fetch NBA game data for a given date.
2. **Transform** — Flattens the nested JSON response into a clean tabular format using pandas, keeping only the relevant columns (teams, scores, date, status).
3. **Load** — Writes the cleaned data into a local SQLite database (`nba_games.db`).

## Tech stack

- **Python** — core language
- **requests** — API calls
- **pandas** — data cleaning and reshaping
- **SQLite** — lightweight local database
- **python-dotenv** — keeps API keys out of source code

## Setup

1. Clone this repo and navigate into the folder.
2. Create a virtual environment: `python -m venv venv`
3. Activate it:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install requests pandas python-dotenv`
5. Get a free API key from [balldontlie.io](https://www.balldontlie.io/)
6. Create a `.env` file in the project root with:
   ```
   BALLDONTLIE_API_KEY=your_key_here
   ```
7. Run the pipeline: `python main.py`

## Output

A SQLite database (`nba_games.db`) with a `games` table containing:

| Column | Description |
|---|---|
| date | Game date |
| home_team / home_abbr | Home team name and abbreviation |
| visitor_team / visitor_abbr | Visiting team name and abbreviation |
| home_team_score / visitor_team_score | Final scores |
| status | Game status (e.g. "Final") |

## What's next

This is Project 1 of 2. Project 2 will build on this by adding:
- Incremental loading (only pulling new games, not re-fetching everything)
- Scheduling/orchestration with Airflow
- Basic error handling and retry logic

## Why I built this

Built to practice the core shape of a data pipeline — extract, transform, load — as part of transitioning from data analysis into data/analytics engineering.
