from datetime import datetime, timedelta
from graded_assignment import GradedAssignment
import json

class Subject:
    def __init__(self, name, passing_grade=60):
        self.name = name
        self.passing_grade = passing_grade
        self.time_studied = timedelta()
        self.time_study_goal = timedelta()
        self.graded_assignments = []

    def add_graded_assignment(self, graded_assignment: GradedAssignment):
        self.graded_assignments.append(graded_assignment)

    def set_time_study_goal(self, goal, goal_deadline: datetime = None):
        self.time_study_goal = goal
        
        if goal_deadline:
            self.goal_deadline = goal_deadline

    def log_study_session(self, time: timedelta):
        self.time_studied += time

    def is_study_time_goal_overdue(self):
        if self.goal_deadline:
            return datetime.now() >= self.goal_deadline
        
        return False

    def has_passing_grade(self):
        return self.current_grade() >= self.passing_grade
    
    def current_grade(self):
        total_grade = 0
        for assignment in self.graded_assignments:
            total_grade += assignment.score
        return total_grade

    def has_met_study_goal(self):
        return self.time_studied >= self.time_study_goal
    
    def to_json(self):
        def timedelta_to_json(timedelta_obj: timedelta):
            timedelta_dict = {"days" : timedelta_obj.days,
                              "seconds" : timedelta_obj.seconds,
                              "microseconds" : timedelta_obj.microseconds}
            return json.dumps(timedelta_dict)
        
        subject_dict = {"name" : self.name,
                        "passing_grade" : self.passing_grade,
                        "time_studied" : timedelta_to_json(self.time_studied),
                        "time_study_goal" : timedelta_to_json(self.time_study_goal),
                        "graded_assignments" : self.graded_assignments_list_to_json(self.graded_assignments)}
        
        return subject_dict
        
    def store(self, file_name='subjects.json'):
        with open(file_name, "w") as subjects_file:
            subjects_file.write(json.dumps(self.to_json()))

    @staticmethod
    def graded_assignments_list_to_json(assignments_list: list[GradedAssignment]):
            assignments_dict = []
            for assignment in assignments_list:
                assignments_dict.append(assignment.to_json())
            return json.dumps(assignments_dict)
        
    def load(self):
        pass
    