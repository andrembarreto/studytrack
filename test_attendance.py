import pytest
import json
from attendance import Attendance

@pytest.fixture
def attendance() -> Attendance:
    return Attendance(60)

def test_should_successfully_update_attendance(attendance: Attendance):
    attendance.update_current_attendance(10)

    assert(attendance.current_attendance == 10)

def test_should_create_attendance_with_current_attendance_zero(attendance: Attendance):
    assert(attendance.current_attendance == 0)

def test_should_raise_value_error_when_update_current_attendance_results_in_negative_value(attendance: Attendance):
    with pytest.raises(ValueError):
        attendance.update_current_attendance(-2)

def test_should_return_minimum_attendance(attendance: Attendance):
    assert(attendance.get_minimum_attendance() == 45)

def test_should_return_false_when_student_does_not_have_minimum_attendance(attendance: Attendance):
    attendance.update_current_attendance(44)
    assert(attendance.has_minimum_attendance() == False)

def test_should_return_true_when_student_has_minimum_attendance(attendance: Attendance):
    attendance.update_current_attendance(45)
    assert(attendance.has_minimum_attendance() == True)

def test_retrieve_attendance_from_json(attendance: Attendance):
    attendance.update_current_attendance(60)
    retrieved_attendance = Attendance.from_json(json.dumps({'workload_hours' : 60, 'current_attendance' : 60, 'minimum_attendance_percentage' : 0.75}))

    assert(retrieved_attendance == attendance)

def test_convert_attendance_to_json_obj(attendance: Attendance):
    json_attendance = Attendance.to_json(attendance)

    expected_json = json.dumps({'workload_hours' : 60, 'current_attendance' : 0, 'minimum_attendance_percentage' : 0.75})
    assert(json_attendance == expected_json)