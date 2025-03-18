import sqlite3

# ✅ Connect to SQLite database
conn = sqlite3.connect("predictions.db", check_same_thread=False)
c = conn.cursor()

# ✅ Create table for storing prediction history
c.execute('''
    CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT NOT NULL,
        disease TEXT NOT NULL,
        result TEXT NOT NULL,
        probability REAL NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
''')
conn.commit()

# ✅ Function to save a prediction
def save_prediction(user, disease, result, probability):
    c.execute("INSERT INTO history (user, disease, result, probability) VALUES (?, ?, ?, ?)",
              (user, disease, result, probability))
    conn.commit()

# ✅ Function to fetch user-specific history
def get_prediction_history(user):
    c.execute("SELECT disease, result, probability, timestamp FROM history WHERE user=? ORDER BY timestamp DESC", (user,))
    return c.fetchall()  # ✅ Returns a list of records


c.execute("SELECT * FROM history")
rows = c.fetchall()

if rows:
    print("🔍 Database Records Found:")
    for row in rows:
        print(row)
else:
    print("⚠️ No records found in the database.")

conn.close()