from datetime import datetime
from graded_assignment import GradedAssignment
import json

def test_can_convert_to_json():
    due_date = datetime.now()
    assignment = GradedAssignment('example_assignment', due_date, 100)
    expected_result = json.dumps({'name' : 'example_assignment',
                                  'date' : due_date.timestamp(),
                                  'max_score' : 100,
                                  'score' : 0})
    
    assert(expected_result == assignment.to_json())