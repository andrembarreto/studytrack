from datetime import datetime, timedelta
from graded_assignment import GradedAssignment
from subject_content import SubjectContent
from attendance import Attendance
import json

class Subject:
    def __init__(self, name, workload, passing_grade=60):
        self.name = name
        self.passing_grade = passing_grade
        self.attendance = Attendance(workload)
        self.time_studied = timedelta()
        self.time_study_goal = timedelta()
        self.graded_assignments = []
        self.contents = []

    def __eq__(self, __value: object):
        return isinstance(__value, Subject) and self.name == __value.name

    def add_graded_assignment(self, graded_assignment: GradedAssignment):
        self.graded_assignments.append(graded_assignment)

    def add_content(self, content: SubjectContent):
        if self.__has_content_with_priority(content.priority):
            raise ValueError(f'There is already a priority {content.priority} content in the subject {self.name}')
        self.contents.append(content)
        self.contents.sort(key=lambda c: c.priority)

    def set_time_study_goal(self, goal, goal_deadline: datetime = None):
        self.time_study_goal = goal
        
        if goal_deadline:
            self.goal_deadline = goal_deadline

    def log_study_session(self, time: timedelta):
        self.time_studied += time

    def is_study_time_goal_overdue(self):
        if hasattr(self, "goal_deadline"):
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
    
    def update_attendance(self, hours):
        self.attendance.update_current_attendance(hours)

    def get_minimum_attendance(self):
        return self.attendance.get_minimum_attendance()
    
    def has_minimum_attendance(self):
        return self.attendance.has_minimum_attendance()
    
    def get_current_attendance(self):
        return self.attendance.current_attendance
    
    def print(self):
        print(f"Name: {self.name}")
        print(f"Passing grade: {self.passing_grade}")
        print(f"Current grade: {self.current_grade()}")
        print(f"Target study time: {self.time_study_goal}")
        print(f"Studied time: {self.time_studied}")
        self.attendance.print()
    
    def to_json(self):
        def timedelta_to_json(timedelta_obj: timedelta):
            timedelta_dict = {"days" : timedelta_obj.days,
                              "seconds" : timedelta_obj.seconds,
                              "microseconds" : timedelta_obj.microseconds}
            return json.dumps(timedelta_dict)
        
        subject_dict = {"name" : self.name,
                        "passing_grade" : self.passing_grade,
                        "attendance" : self.attendance.to_json(),
                        "time_studied" : timedelta_to_json(self.time_studied),
                        "time_study_goal" : timedelta_to_json(self.time_study_goal),
                        "graded_assignments" : self.graded_assignments_list_to_json(self.graded_assignments),
                        "subject_contents": self.subject_contents_list_to_json(self.contents)}
        
        return json.dumps(subject_dict)
    
    @staticmethod
    def from_json(json_obj):
        def timedelta_from_json(timedelta_obj):
            return timedelta(days=timedelta_obj.get('days'),
                             seconds=timedelta_obj.get('seconds'),
                             microseconds=timedelta_obj.get('microseconds'))
        
        json_obj = json.loads(json_obj)

        subject = Subject(name=json_obj.get('name'), workload=0, passing_grade=json_obj.get('passing_grade'))
        subject.attendance = Attendance.from_json(json_obj.get('attendance'))
        subject.time_studied = timedelta_from_json(json.loads(json_obj.get('time_studied')))
        subject.time_study_goal = timedelta_from_json(json.loads(json_obj.get('time_study_goal')))
        
        for content in json.loads(json_obj.get('subject_contents')):
            subject.add_content(SubjectContent.from_json(content))
        
        for assignment in json.loads(json_obj.get('graded_assignments')):
            subject.add_graded_assignment(GradedAssignment.from_json(assignment))

        return subject
    
    def __has_content_with_priority(self, priority):
        for content in self.contents:
            if content.priority == priority:
                return True
        return False

    @staticmethod
    def graded_assignments_list_to_json(assignments_list: list[GradedAssignment]):
        assignments_dict = []
        for assignment in assignments_list:
            assignments_dict.append(assignment.to_json())
        return json.dumps(assignments_dict)
    
    @staticmethod
    def subject_contents_list_to_json(subject_contents: list[SubjectContent]):
        content_dict = []
        for content in subject_contents:
            content_dict.append(content.to_json())
        return json.dumps(content_dict)
