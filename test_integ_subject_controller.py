import pytest
import os

from datetime import datetime, timedelta
from subject_controller import SubjectController, Subject
from graded_assignment import GradedAssignment
from subject_content import SubjectContent

@pytest.fixture
def subject_60_hours() -> Subject:
    subject = Subject('example_subject', 60)
    subject.add_content(SubjectContent('Teste', 5))
    subject.add_graded_assignment(GradedAssignment('prova', datetime.now(), 30, 30))
    return subject

@pytest.fixture
def file_deleter() -> None:
    yield None
    os.remove('test_controller.json')

def test_adding_subject_is_persistent(subject_60_hours: Subject, file_deleter):
    controller = SubjectController()
    
    # add subject
    controller.add_subject(subject_60_hours)

    # store subjects list
    controller.store(file_name='test_controller.json')

    # load stored subjects list
    controller.load(file_name='test_controller.json')

    # check for added subject
    assert(subject_60_hours in controller.subjects_list)

def test_removing_subject_is_persistent(subject_60_hours: Subject, file_deleter):
    controller = SubjectController()
    controller.add_subject(subject_60_hours)

    controller.store(file_name='test_controller.json')

    controller.load(file_name='test_controller.json')

    assert(subject_60_hours in controller.subjects_list)

    controller.remove_subject(subject_60_hours)

    controller.store('test_controller.json')

    controller.load(file_name='test_controller.json')
    assert(subject_60_hours not in controller.subjects_list)

def test_removing_subject_that_was_not_stored(subject_60_hours: Subject):
    controller = SubjectController()

    controller.load('test_controller.json')

    with pytest.raises(ValueError):
        controller.remove_subject(subject_60_hours)

def test_check_for_enough_credits_to_graduate(subject_60_hours):
    controller = SubjectController()

    subject_60_hours.update_attendance(45)

    second_subject_60_hours = Subject('second_example', 60)
    second_subject_60_hours.update_attendance(45)
    
    minimal_credits_to_graduate = 8
    credit_conversion_method = lambda x: x / 4

    controller.add_subject(subject_60_hours)
    controller.add_subject(second_subject_60_hours)

    assert(controller.has_enough_credits_to_graduate(minimal_credits_to_graduate, credit_conversion_method))
