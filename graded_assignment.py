from datetime import datetime
import json

class GradedAssignment:
    def __init__(self, name, date: datetime, maximum_score, score=0):
        self.name = name
        self.date = date
        self.maximum_score = maximum_score
        self.score = score

    def get_percentage_grade(self):
        return self.score / self.maximum_score
    
    def update_date(self, new_date: datetime):
        self.date = new_date

    def to_json(self):
        self_dict = {"name" : self.name,
                     "date" : self.date.timestamp(),
                     "max_score" : self.maximum_score,
                     "score" : self.score}
        return json.dumps(self_dict)