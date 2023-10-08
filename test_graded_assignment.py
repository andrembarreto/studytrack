from datetime import datetime, timedelta
from graded_assignment import GradedAssignment
import json

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