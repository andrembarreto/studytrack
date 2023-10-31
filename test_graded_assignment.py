import pytest
from datetime import datetime, timedelta
from graded_assignment import GradedAssignment
import json

def test_should_calculate_and_return_percentage_grade():
    graded_assignment = GradedAssignment('assignment', datetime(2001, 1, 1, 0, 0, 0, 1), 25, 20)

    assert(graded_assignment.get_percentage_grade() == 0.8)

def test_should_not_be_able_to_create_assignment_with_null_grade():
    with pytest.raises(ValueError):
        graded_assignment = GradedAssignment('assignment', datetime.now(), 0)

def test_should_not_be_able_to_create_assignment_with_negative_grade():
    with pytest.raises(ValueError):
        graded_assignment = GradedAssignment('assignment', datetime.now(), -1)

def test_should_get_null_percentage_if_mistakenly_changes_max_score_to_0():
    graded_assignment = GradedAssignment('assignment', datetime.now(), 10)
    graded_assignment.maximum_score = 0 # never do this
    
    assert(graded_assignment.get_percentage_grade() == 0)

def test_should_update_date():
    graded_assignment = GradedAssignment('assignment', datetime(2001, 1, 1, 0, 0, 0, 1), 25, 20)
    new_datetime = datetime(2023, 1, 1, 0, 0, 0, 1)

    graded_assignment.update_date(new_datetime)
    
    assert(graded_assignment.date == new_datetime)

def test_assignments_should_be_considered_equals():
    common_datetime = datetime(2001, 1, 1, 0, 0, 0, 1)

    first_assignment = GradedAssignment('assignment_A', common_datetime, 20, 5)
    second_assignment = GradedAssignment('assignment_A', common_datetime, 30, 10)

    assert(first_assignment == second_assignment)

def test_assignments_with_different_dates_should_be_considered_different():
    common_datetime = datetime(2001, 1, 1, 0, 0, 0, 1)

    first_assignment = GradedAssignment('assignment_A', common_datetime, 20, 5)
    second_assignment = GradedAssignment('assignment_A', common_datetime + timedelta(days=1), 20, 5)

    assert(not first_assignment == second_assignment)

def test_assignments_with_different_names_should_be_considered_different():
    common_datetime = datetime(2001, 1, 1, 0, 0, 0, 1)

    first_assignment = GradedAssignment('assignment_A', common_datetime, 20, 5)
    second_assignment = GradedAssignment('assignment_B', common_datetime, 20, 5)

    assert(not first_assignment == second_assignment)

def test_can_convert_to_json():
    due_date = datetime.now()
    assignment = GradedAssignment('example_assignment', due_date, 100)
    expected_result = json.dumps({'name' : 'example_assignment',
                                  'date' : due_date.timestamp(),
                                  'max_score' : 100,
                                  'score' : 0})
    
    assert(expected_result == assignment.to_json())

def test_can_retrieve_assignment_from_json_obj():
    due_date = datetime.now()
    original_assignment = GradedAssignment('example_assignment', due_date, 50, 25)
    
    retrieved_assignment = GradedAssignment.from_json(original_assignment.to_json())

    assert(retrieved_assignment == original_assignment)