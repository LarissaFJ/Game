import os
from code.DBProxy import DBProxy

class ScoreManager:
    def __init__(self):
        os.makedirs("score", exist_ok=True)
        self.db = DBProxy("score/scores.db")
    
    def save_score(self, player_name, score):
        self.db.save_score(player_name, score)
    
    def load_scores(self):
        results = self.db.get_top_scores()
        return [{"name": row[0], "score": row[1]} for row in results]
    
    def clear_scores(self):
        self.db.clear_scores()