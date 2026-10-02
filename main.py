import requests
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("BALLDONTLIE_API_KEY")  # paste your key between the quotes
response = requests.get(
    "https://api.balldontlie.io/v1/games",
    headers={"Authorization": API_KEY},
    params={"dates[]": "2026-01-15"}  # pick any past date with NBA games
)

# print(response.status_code)
# print(response.text)

print(response.json())

# ================================================================
import pandas as pd
games = response.json()["data"]

df = pd.json_normalize(games)

print(df.columns.tolist())

# ================================================================
import sqlite3

# Select only the columns we need
columns_needed = [
    "date",
    "home_team.full_name", "home_team.abbreviation",
    "visitor_team.full_name", "visitor_team.abbreviation",
    "home_team_score", "visitor_team_score",
    "status"
]
df_clean = df[columns_needed]

# Rename columns to something simpler (optional but tidier)
df_clean = df_clean.rename(columns={
    "home_team.full_name": "home_team",
    "home_team.abbreviation": "home_abbr",
    "visitor_team.full_name": "visitor_team",
    "visitor_team.abbreviation": "visitor_abbr"
})

# Connect to (or create) a SQLite database file
conn = sqlite3.connect("nba_games.db")

# Write the dataframe to a table called "games"
df_clean.to_sql("games", conn, if_exists="replace", index=False)

conn.close()

print("Saved to nba_games.db")
