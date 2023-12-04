from subject import Subject
import json
import os

class SubjectController():
    def __init__(self):
        self.subjects = {}

    def add_subject(self, subject: Subject):
        if self.subject_already_exists(subject):
            raise ValueError('This subject already exists')
        
        self.subjects[subject.name] = subject

    def remove_subject(self, subject_name):
        self.subjects.pop(subject_name)

    def subject_already_exists(self, subject: Subject):
        return subject.name in self.subjects.keys()
    
    def get_average_term_grade(self):
        if len(self.subjects) == 0:
            return 0
        
        total = 0
        for subject in self.subjects.values():
            total += subject.current_grade()

        average_term_grade = total / len(self.subjects)
        return average_term_grade
    
    def get_current_term_credits(self, credit_conversion_method = lambda x: x):
        total_credits = 0

        for subject in self.subjects.values():
            if (subject.has_minimum_attendance() and subject.has_passing_grade()):
                total_credits += credit_conversion_method(subject.attendance.workload_hours)

        return total_credits
    
    def has_enough_credits_to_graduate(self, minimal_credits, credit_conversion_method = lambda x: x):
        return self.get_current_term_credits(credit_conversion_method) >= minimal_credits
    
    def filter_by_passing_grade(self, has_passing_grade: bool):
        filtered_subjects = {}

        for subject in self.subjects.values():
            if (has_passing_grade and subject.has_passing_grade()) or (not has_passing_grade and not subject.has_passing_grade()):
                filtered_subjects[subject.name] = subject

        return filtered_subjects

    def filter_by_study_goal_overdue(self, study_goal_overdue: bool):
        filtered_subjects = {}

        for subject in self.subjects.values():
            if (study_goal_overdue and subject.is_study_time_goal_overdue()) or (not study_goal_overdue and not subject.is_study_time_goal_overdue()):
                filtered_subjects[subject.name] = subject

        return filtered_subjects
    
    def update_subject_attendance(self, subject_name, hours):
        self.subjects[subject_name].update_attendance(hours)

    def store(self, file_name='subjects.json', filter: str = None, include_flag: bool = True):
        '''Filter Options: "passing_grade" | "study_goal" '''
        
        filter_options = {
            'passing_grade': self.filter_by_passing_grade,
            'study_goal': self.filter_by_study_goal_overdue
        }

        with open(file_name, 'w') as subjects_file:
            if filter is not None:
                subjects_to_save = filter_options[filter](include_flag)
                subjects_file.write(self.to_json(subjects_to_save))
            else:
                subjects_file.write(self.to_json())

        subjects_file.close()

    def to_json(self, subjects_to_save = None):
        if subjects_to_save is None:
            subjects_to_save = self.subjects
            
        subjects_dict = {}

        for subject in subjects_to_save.values():
            subjects_dict[subject.name] = subject.to_json()

        return json.dumps(subjects_dict, indent=2)

    def load(self, file_name='subjects.json'):
        if os.path.exists(file_name):
            subjects_file = open(file_name, 'r')
            subjects = dict(json.loads(subjects_file.read()))

            subjects_file.close()

            self.subjects = {}
    
            for subject in subjects.values():
                subject = Subject.from_json(subject)
                self.subjects[subject.name] = subject
