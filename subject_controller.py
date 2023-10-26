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