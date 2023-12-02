from subject import Subject
import json
import os

class SubjectController():
    def __init__(self):
        self.subjects_list = []

    def add_subject(self, subject: Subject):
        if self.subject_already_exists(subject):
            raise ValueError('This subject already exists')
        
        self.subjects_list.append(subject)

    def remove_subject(self, subject: Subject):
        if not self.subject_already_exists(subject):
            raise ValueError('This subject does not exists')
        
        self.subjects_list.remove(subject)

    def subject_already_exists(self, subject: Subject):
        return subject in self.subjects_list
    
    def get_average_term_grade(self):
        if len(self.subjects_list) == 0:
            return 0
        
        total = 0
        for subject in self.subjects_list:
            total += subject.current_grade()

        average_term_grade = total / len(self.subjects_list)
        return average_term_grade
    
    def get_current_term_credits(self, credit_conversion_method = lambda x: x):
        total_credits = 0

        for subject in self.subjects_list:
            if (subject.has_minimum_attendance()):
                total_credits += credit_conversion_method(subject.attendance.workload_hours)

        return total_credits
    
    def has_enough_credits_to_graduate(self, minimal_credits, credit_conversion_method = lambda x: x):
        return self.get_current_term_credits(credit_conversion_method) >= minimal_credits
    
    def find_by_name(self, subjectName):
        for subject in self.subjects_list:
            if subject.name == subjectName:
                return subject
        
        raise ValueError(f'Subject {subjectName} not found')
    
    def filter_by_passing_grade(self, has_passing_grade: bool):
        filtered_subjects = []

        for subject in self.subjects_list:
            if (has_passing_grade and subject.has_passing_grade()) or (not has_passing_grade and not subject.has_passing_grade()):
                filtered_subjects.append(subject)

        return filtered_subjects

    def filter_by_study_goal_overdue(self, study_goal_overdue: bool):
        filtered_subjects = []

        for subject in self.subjects_list:
            if (study_goal_overdue and subject.is_study_time_goal_overdue()) or (not study_goal_overdue and not subject.is_study_time_goal_overdue()):
                filtered_subjects.append(subject)

        return filtered_subjects

    def store(self, file_name='subjects.json'):
        with open(file_name, 'w') as subjects_file:
            subjects_file.write(self.to_json())

        subjects_file.close()

    def to_json(self):
        subjects_dict = {}

        for subject in self.subjects_list:
            subjects_dict[subject.name] = subject.to_json()

        return json.dumps(subjects_dict, indent=2)

    def load(self, file_name='subjects.json'):
        if os.path.exists(file_name):
            with open(file_name, 'r') as subjects_file:
                subjects = dict(json.loads(subjects_file.read()))

            subjects_file.close()

            subjects_list = []
            for (_, subject_obj) in subjects.items():
                subjects_list.append(Subject.from_json(subject_obj))

            self.subjects_list = subjects_list
    