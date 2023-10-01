from datetime import datetime, timedelta
from graded_assignment import GradedAssignment

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
    
    def store(self):
        pass

    def load(self):
        pass
    