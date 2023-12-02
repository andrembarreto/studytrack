import pytest
import os

from datetime import datetime, timedelta
from subject_controller import SubjectController, Subject
from graded_assignment import GradedAssignment
from subject_content import SubjectContent

@pytest.fixture
def subject_30_hours() -> Subject:
    subject = Subject('example_subject', 30, 60)
    subject.add_content(SubjectContent('Teste', 5))
    subject.add_graded_assignment(GradedAssignment('prova', datetime.now(), 30, 30))
    return subject

@pytest.fixture
def file_deleter() -> None:
    yield None
    os.remove('test_controller.json')

def test_adding_subject_is_persistent(subject_30_hours: Subject, file_deleter):
    controller = SubjectController()
    
    # add subject
    controller.add_subject(subject_30_hours)

    # store subjects list
    controller.store(file_name='test_controller.json')

    # load stored subjects list
    retrieved_subjects_list = controller.load(file_name='test_controller.json')

    # check for added subject
    assert(subject_30_hours in retrieved_subjects_list)
