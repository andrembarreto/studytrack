import pytest
from datetime import datetime, timedelta
from subject_controller import SubjectController, Subject
from graded_assignment import GradedAssignment

@pytest.fixture
def subject_controller() -> SubjectController:
    return SubjectController()

@pytest.fixture
def subject_science() -> Subject:
    return Subject('science', 100)

@pytest.fixture
def subject_english() -> Subject:
    return Subject('english', 50)

def test_should_be_able_to_add_subjects_with_different_names(subject_controller, subject_science, subject_english):
    subject_controller.add_subject(subject_science)
    assert(subject_science in subject_controller.subjects_list)
    
    subject_controller.add_subject(subject_english)
    assert(subject_english in subject_controller.subjects_list)

def test_should_not_be_able_to_add_subject_with_repeated_name(subject_controller, subject_science):
    subject_controller.add_subject(subject_science)

    with pytest.raises(ValueError):
        subject_controller.add_subject(subject_science)

def test_can_remove_added_subject(subject_controller, subject_science):
    subject_controller.add_subject(subject_science)
    assert(subject_science in subject_controller.subjects_list)

    subject_controller.remove_subject(subject_science)
    assert(subject_science not in subject_controller.subjects_list)

def test_cannot_remove_subject_not_added(subject_controller, subject_science):
    with pytest.raises(ValueError):
        subject_controller.remove_subject(subject_science)

def test_should_find_subject_by_name(subject_controller, subject_science, subject_english):
    subject_controller.add_subject(subject_science)
    subject_controller.add_subject(subject_english)

    found_subject = subject_controller.find_by_name('science')

    assert(found_subject == subject_science)

def test_should_raise_value_error_when_subject_with_searched_name_is_not_saved(subject_controller):
    with pytest.raises(ValueError):
        subject_controller.find_by_name('science')

def test_should_return_subjects_in_which_student_has_passing_grade(subject_controller, subject_english, subject_science):
    graded_assignment = GradedAssignment('assignment', datetime(2001, 1, 1, 0, 0, 0, 1), 100, 60)

    subject_english.add_graded_assignment(graded_assignment)

    subject_controller.add_subject(subject_english)
    subject_controller.add_subject(subject_science)

    filtered_subjects = subject_controller.filter_by_passing_grade(has_passing_grade=True)

    assert(filtered_subjects.__len__() == 1)
    assert(filtered_subjects[0] == subject_english)

def test_should_return_subjects_in_which_student_has_not_passing_grade(subject_controller, subject_english, subject_science):
    graded_assignment = GradedAssignment('assignment', datetime(2001, 1, 1, 0, 0, 0, 1), 100, 60)

    subject_english.add_graded_assignment(graded_assignment)

    subject_controller.add_subject(subject_english)
    subject_controller.add_subject(subject_science)

    filtered_subjects = subject_controller.filter_by_passing_grade(has_passing_grade=False)

    assert(filtered_subjects.__len__() == 1)
    assert(filtered_subjects[0] == subject_science)

def test_should_return_empty_when_searching_has_passing_grade_and_student_not_passed_in_any_subject(subject_controller, subject_english, subject_science):
    subject_controller.add_subject(subject_english)
    subject_controller.add_subject(subject_science)

    filtered_subjects = subject_controller.filter_by_passing_grade(has_passing_grade=True)

    assert(filtered_subjects.__len__() == 0)

def test_should_return_empty_when_searching_has_not_passing_grade_and_student_passed_in_all_subjects(subject_controller, subject_english, subject_science):
    graded_assignment = GradedAssignment('assignment', datetime(2001, 1, 1, 0, 0, 0, 1), 100, 60)

    subject_science.add_graded_assignment(graded_assignment)
    subject_english.add_graded_assignment(graded_assignment)

    subject_controller.add_subject(subject_english)
    subject_controller.add_subject(subject_science)

    filtered_subjects = subject_controller.filter_by_passing_grade(has_passing_grade=False)

    assert(filtered_subjects.__len__() == 0)

def test_should_return_subjects_which_study_time_goal_is_overdue(subject_controller, subject_english, subject_science):
    overdue_date = datetime(2000, 1, 1, 0, 0, 0, 0)

    valid_date = datetime.today() + timedelta(days=1)

    subject_science.set_time_study_goal(10, overdue_date)
    subject_english.set_time_study_goal(10, valid_date)

    subject_controller.add_subject(subject_science)
    subject_controller.add_subject(subject_english)

    filtered_subjects = subject_controller.filter_by_study_goal_overdue(True)

    assert(filtered_subjects.__len__() == 1)
    assert(filtered_subjects[0] == subject_science)

def test_should_return_subjects_which_study_time_goal_is_not_overdue(subject_controller, subject_english, subject_science):
    overdue_date = datetime(2000, 1, 1, 0, 0, 0, 0)

    valid_date = datetime.today() + timedelta(days=1)

    subject_science.set_time_study_goal(10, overdue_date)
    subject_english.set_time_study_goal(10, valid_date)

    subject_controller.add_subject(subject_science)
    subject_controller.add_subject(subject_english)

    filtered_subjects = subject_controller.filter_by_study_goal_overdue(False)

    assert(filtered_subjects.__len__() == 1)
    assert(filtered_subjects[0] == subject_english)

def test_should_return_empty_when_there_is_no_subject_with_study_time_goal_overdue(subject_controller, subject_english):
    valid_date = datetime.today() + timedelta(days=1)

    subject_english.set_time_study_goal(10, valid_date)

    subject_controller.add_subject(subject_english)

    filtered_subjects = subject_controller.filter_by_study_goal_overdue(True)

    assert(filtered_subjects.__len__() == 0)

def test_should_return_empty_when_all_subjects_study_time_goal_overdue(subject_controller, subject_english):
    overdue_date = datetime(2000, 1, 1, 0, 0, 0, 0)

    subject_english.set_time_study_goal(10, overdue_date)

    subject_controller.add_subject(subject_english)

    filtered_subjects = subject_controller.filter_by_study_goal_overdue(False)

    assert(filtered_subjects.__len__() == 0)
