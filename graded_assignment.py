from datetime import datetime

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