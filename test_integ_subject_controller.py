import pytest
import os

from datetime import datetime
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
def test_file() -> str:
    file_name = 'test_controller.json'
    yield file_name
    os.remove(file_name)

def test_adding_subject_is_persistent(subject_60_hours: Subject, test_file):
    controller = SubjectController()
    
    # add subject
    controller.add_subject(subject_60_hours)

    # store subjects list
    controller.store(file_name=test_file)

    # load stored subjects list
    controller.load(file_name=test_file)

    # check for added subject
    assert(subject_60_hours in controller.subjects.values())

def test_removing_subject_is_persistent(subject_60_hours: Subject, test_file):
    controller = SubjectController()
    controller.add_subject(subject_60_hours)

    controller.store(file_name=test_file)

    controller.load(file_name=test_file)

    assert(subject_60_hours in controller.subjects.values())

    controller.remove_subject(subject_60_hours)

    controller.store(test_file)

    controller.load(file_name=test_file)
    assert(subject_60_hours not in controller.subjects.values())

def test_removing_subject_that_was_not_stored(subject_60_hours: Subject):
    controller = SubjectController()

    controller.load('test_file.json')

    with pytest.raises(KeyError):
        controller.remove_subject(subject_60_hours)

def test_check_for_enough_credits_to_graduate(subject_60_hours: Subject):
    controller = SubjectController()

    subject_60_hours.add_graded_assignment(GradedAssignment('Exam', datetime.now(), 100, 60))

    second_subject_60_hours = Subject('second_example', 60)
    second_subject_60_hours.add_graded_assignment(GradedAssignment('Exam', datetime.now(), 100, 60))
    
    minimal_credits_to_graduate = 8
    credit_conversion_method = lambda x: x / 4

    controller.add_subject(subject_60_hours)
    controller.add_subject(second_subject_60_hours)
    controller.update_subject_attendance(subject_60_hours.name, 45)
    controller.update_subject_attendance(second_subject_60_hours.name, 45)


    assert(controller.has_enough_credits_to_graduate(minimal_credits_to_graduate, credit_conversion_method))

def test_store_only_subjects_without_passing_grade_in_separate_file(test_file):
    
    subject_science = Subject('Science', 60)
    subject_science.add_graded_assignment(GradedAssignment('Exam', datetime.now(), 100, 80))

    subject_english = Subject('English', 60)
    subject_english.add_graded_assignment(GradedAssignment('Exam', datetime.now(), 100, 50))

    controller = SubjectController()

    controller.add_subject(subject_science)
    controller.add_subject(subject_english)
    
    controller.store(test_file, filter='passing_grade', include_flag=False)
    
    controller.load(test_file)

    assert(subject_english in controller.subjects.values())
    assert(subject_science not in controller.subjects.values())
