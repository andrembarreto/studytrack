from datetime import datetime
import json

class GradedAssignment:
    def __init__(self, name, date: datetime, maximum_score, score=0):
        if (maximum_score <= 0):
            raise ValueError('A graded assignment should have a positive grade value')
        
        self.name = name
        self.date = date
        self.maximum_score = maximum_score
        self.score = score

    def __eq__(self, __value: object):
        def same_day_dates(first_date: datetime, second_date: datetime):
            return first_date.day == second_date.day and first_date.month == second_date.month and first_date.year == second_date.year
        
        return isinstance(__value, GradedAssignment) and self.name == __value.name and same_day_dates(self.date, __value.date)

    def get_percentage_grade(self):
        try:
            percentage_grade = self.score / self.maximum_score
        
        except ZeroDivisionError: # ideally should not happen, but max score might have been directly altered
            return 0

        return percentage_grade
    
    def update_date(self, new_date: datetime):
        self.date = new_date

    def to_json(self):
        self_dict = {"name" : self.name,
                     "date" : self.date.timestamp(),
                     "max_score" : self.maximum_score,
                     "score" : self.score}
        return json.dumps(self_dict)
    
    @staticmethod
    def from_json(json_obj):
        json_obj = json.loads(json_obj)
        assignment = GradedAssignment(name=json_obj.get('name'), date=datetime.fromtimestamp(json_obj.get('date')), 
                                      maximum_score=json_obj.get('max_score'), score=json_obj.get('score'))
        
        return assignment
        
