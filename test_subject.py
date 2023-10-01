import pytest
from subject import Subject, GradedAssignment, SubjectContent
from datetime import datetime, timedelta
import json
import os

# unit tests

def test_can_identify_meeting_study_goal():
    subject = Subject('example_subject')
    
    subject.set_time_study_goal(timedelta(hours=10))
    
    subject.log_study_session(timedelta(hours=5))
    subject.log_study_session(timedelta(hours=5))

    assert(subject.has_met_study_goal())

def test_can_identify_not_meeting_study_goal():
    subject = Subject('example_subject')
    
    subject.set_time_study_goal(timedelta(hours=10))
    
    subject.log_study_session(timedelta(hours=5))
    subject.log_study_session(timedelta(hours=4))

    assert(not subject.has_met_study_goal())

def test_can_identify_passing_grade():
    subject = Subject('example_subject', 60)
    commom_datetime = datetime(2000, 1, 1, 0, 0, 0, 1)

    subject.add_graded_assignment(GradedAssignment('assignment_A', commom_datetime, 50, 25))
    subject.add_graded_assignment(GradedAssignment('assignment_B', commom_datetime, 50, 35))

    assert(subject.has_passing_grade())

def test_can_identify_failing_grade():
    subject = Subject('example_subject', 60)
    commom_datetime = datetime(2000, 1, 1, 0, 0, 0, 1)

    subject.add_graded_assignment(GradedAssignment('assignment_A', commom_datetime, 50, 25))
    subject.add_graded_assignment(GradedAssignment('assignment_B', commom_datetime, 50, 34))

    assert(not subject.has_passing_grade())

def test_can_identify_study_time_goal_overdue():
    subject = Subject('example_subject')
    
    subject.set_time_study_goal(timedelta(hours=10), datetime.now() - timedelta(days=1))
    
    assert(subject.is_study_time_goal_overdue())

def test_can_identify_study_time_goal_not_overdue():
    subject = Subject('example_subject')
    
    subject.set_time_study_goal(timedelta(hours=10), datetime.now() + timedelta(days=1))
    
    assert(not subject.is_study_time_goal_overdue())

def test_can_add_subject_content_sorting_by_priority():
    subject = Subject('example_subject')
    
    subject.add_content(SubjectContent('content_A', 2))
    subject.add_content(SubjectContent('content_B', 1))

    assert(subject.contents[0].priority == 1)

# integration tests

def test_can_store_subject():
    subject = Subject('example_subject')
    commom_datetime = datetime(2000, 1, 1, 0, 0, 0, 1)

    subject.add_graded_assignment(GradedAssignment('assignment_A', commom_datetime, 50, 25))
    subject.add_graded_assignment(GradedAssignment('assignment_B', commom_datetime, 50, 34))

    subject.add_content(SubjectContent('content_A', 1))
    subject.add_content(SubjectContent('content_B', 2))

    subject.store('test_subjects.json')

    test_file = open('test_subjects.json', 'r')
    stored_content = json.loads(test_file.read())

    test_file.close()

    expected_result = subject.to_json()

    assert(expected_result == stored_content)

    os.remove('test_subjects.json')