import pytest
from subject import Subject, GradedAssignment, SubjectContent
from datetime import datetime, timedelta
import json
import os

# unit tests

@pytest.fixture
def subject_30_hours() -> Subject:
    return Subject('example_subject', 30)

def test_can_identify_meeting_study_goal(subject_30_hours):
    subject_30_hours.set_time_study_goal(timedelta(hours=10))
    
    subject_30_hours.log_study_session(timedelta(hours=5))
    subject_30_hours.log_study_session(timedelta(hours=5))

    assert(subject_30_hours.has_met_study_goal())

def test_can_identify_not_meeting_study_goal(subject_30_hours):
    subject_30_hours.set_time_study_goal(timedelta(hours=10))
    
    subject_30_hours.log_study_session(timedelta(hours=5))
    subject_30_hours.log_study_session(timedelta(hours=4))

    assert(not subject_30_hours.has_met_study_goal())

def test_can_identify_passing_grade():
    subject = Subject('example_subject', 30, 60)
    commom_datetime = datetime(2000, 1, 1, 0, 0, 0, 1)

    subject.add_graded_assignment(GradedAssignment('assignment_A', commom_datetime, 50, 25))
    subject.add_graded_assignment(GradedAssignment('assignment_B', commom_datetime, 50, 35))

    assert(subject.has_passing_grade())

def test_can_identify_failing_grade():
    subject = Subject('example_subject', 30, 60)
    commom_datetime = datetime(2000, 1, 1, 0, 0, 0, 1)

    subject.add_graded_assignment(GradedAssignment('assignment_A', commom_datetime, 50, 25))
    subject.add_graded_assignment(GradedAssignment('assignment_B', commom_datetime, 50, 34))

    assert(not subject.has_passing_grade())

def test_can_identify_study_time_goal_overdue(subject_30_hours):
    subject_30_hours.set_time_study_goal(timedelta(hours=10), datetime.now() - timedelta(days=1))
    
    assert(subject_30_hours.is_study_time_goal_overdue())

def test_can_identify_study_time_goal_not_overdue(subject_30_hours):
    subject_30_hours.set_time_study_goal(timedelta(hours=10), datetime.now() + timedelta(days=1))
    
    assert(not subject_30_hours.is_study_time_goal_overdue())

def test_goal_should_not_be_overdue_if_no_date_is_set(subject_30_hours):
    subject_30_hours.set_time_study_goal(timedelta(hours=10))

    assert(not subject_30_hours.is_study_time_goal_overdue())
   
def test_can_add_subject_content_sorting_by_priority(subject_30_hours):
    subject_30_hours.add_content(SubjectContent('content_A', 2))
    subject_30_hours.add_content(SubjectContent('content_B', 1))

    assert(subject_30_hours.contents[0].priority == 1)

def test_should_raise_error_when_adding_content_with_priority_already_added(subject_30_hours):
    subject_30_hours.add_content(SubjectContent('content_A', 1))

    with pytest.raises(ValueError):
        subject_30_hours.add_content(SubjectContent('content_B', 1))

def test_retrieve_subject_without_assignments_or_contents_from_json_obj(subject_30_hours):
    retrieved_subject = Subject.from_json(subject_30_hours.to_json())

    assert(retrieved_subject == subject_30_hours)

def test_retrieve_subject_with_assignments_from_json_obj(subject_30_hours):
    commom_datetime = datetime(2000, 1, 1, 0, 0, 0, 1)

    subject_30_hours.add_graded_assignment(GradedAssignment('assignment_A', commom_datetime, 50, 25))
    subject_30_hours.add_graded_assignment(GradedAssignment('assignment_B', commom_datetime, 50, 34))

    retrieved_subject = Subject.from_json(subject_30_hours.to_json())

    assert(retrieved_subject == subject_30_hours)

def test_retrieve_subject_with_contents_from_json_obj(subject_30_hours):
    subject_30_hours.add_content(SubjectContent('content_A', 1))
    subject_30_hours.add_content(SubjectContent('content_B', 2))

    retrieved_subject = Subject.from_json(subject_30_hours.to_json())

    assert(retrieved_subject == subject_30_hours)

def test_should_successfully_update_attendance(subject_30_hours):
    subject_30_hours.update_attendance(10)

    assert(subject_30_hours.get_current_attendance() == 10)

def test_should_return_minimum_attendance(subject_30_hours):
    assert(subject_30_hours.get_minimum_attendance() == 22)

def test_should_return_false_when_student_does_not_have_minimum_attendance(subject_30_hours):
    subject_30_hours.update_attendance(21)
    assert(subject_30_hours.has_minimum_attendance() == False)

def test_should_return_true_when_student_has_minimum_attendance(subject_30_hours):
    subject_30_hours.update_attendance(22)
    assert(subject_30_hours.has_minimum_attendance() == True)