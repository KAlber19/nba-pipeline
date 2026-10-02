import sqlite3

conn = sqlite3.connect("nba_games.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM games LIMIT 5")
rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()