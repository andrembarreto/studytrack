from subject import Subject

class SubjectController():
    def __init__(self):
        self.subjects_list = []

    def add_subject(self, subject: Subject):
        if self.subject_already_exists(subject):
            raise ValueError('This subject already exists')
        
        self.subjects_list.append(subject)

    def remove_subject(self, subject: Subject):
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
    