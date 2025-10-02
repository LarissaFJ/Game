import sqlite3


class DBProxy():
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()
    
    def create_tables(self):
        self.execute("""
            CREATE TABLE IF NOT EXISTS scores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player_name TEXT NOT NULL,
                score INTEGER NOT NULL
            )
        """)
    
    def save_score(self, player_name, score):
        self.execute("INSERT INTO scores (player_name, score) VALUES (?, ?)", (player_name, score))
    
    def get_top_scores(self):
        self.execute("SELECT player_name, score FROM scores ORDER BY score DESC LIMIT 5")
        return self.fetchall()
    
    def clear_scores(self):
        self.execute("DELETE FROM scores")
    
    def execute(self, query: str, params=None):
        if params:
            self.cursor.execute(query, params)
        else:
            self.cursor.execute(query)
        self.connection.commit()
    
    def fetchall(self):
        return self.cursor.fetchall()
    
    def close(self):
        self.connection.close()