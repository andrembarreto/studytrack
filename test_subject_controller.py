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
    assert(subject_science in subject_controller.subjects.values())
    
    subject_controller.add_subject(subject_english)
    assert(subject_english in subject_controller.subjects.values())

def test_should_not_be_able_to_add_subject_with_repeated_name(subject_controller, subject_science):
    subject_controller.add_subject(subject_science)

    with pytest.raises(ValueError):
        subject_controller.add_subject(subject_science)

def test_can_remove_added_subject(subject_controller, subject_science):
    subject_controller.add_subject(subject_science)
    assert(subject_science in subject_controller.subjects.values())

    subject_controller.remove_subject(subject_science.name)
    assert(subject_science not in subject_controller.subjects.values())

def test_should_return_subjects_in_which_student_has_passing_grade(subject_controller, subject_english, subject_science):
    graded_assignment = GradedAssignment('assignment', datetime(2001, 1, 1, 0, 0, 0, 1), 100, 60)

    subject_english.add_graded_assignment(graded_assignment)

    subject_controller.add_subject(subject_english)
    subject_controller.add_subject(subject_science)

    filtered_subjects = subject_controller.filter_by_passing_grade(has_passing_grade=True)

    assert(len(filtered_subjects) == 1)
    assert(subject_english in filtered_subjects.values())

def test_should_return_subjects_in_which_student_has_not_passing_grade(subject_controller, subject_english, subject_science):
    graded_assignment = GradedAssignment('assignment', datetime(2001, 1, 1, 0, 0, 0, 1), 100, 60)

    subject_english.add_graded_assignment(graded_assignment)

    subject_controller.add_subject(subject_english)
    subject_controller.add_subject(subject_science)

    filtered_subjects = subject_controller.filter_by_passing_grade(has_passing_grade=False)

    assert(len(filtered_subjects) == 1)
    assert(subject_science in filtered_subjects.values())

def test_should_return_empty_when_searching_has_passing_grade_and_student_not_passed_in_any_subject(subject_controller, subject_english, subject_science):
    subject_controller.add_subject(subject_english)
    subject_controller.add_subject(subject_science)

    filtered_subjects = subject_controller.filter_by_passing_grade(has_passing_grade=True)

    assert(len(filtered_subjects) == 0)

def test_should_return_empty_when_searching_has_not_passing_grade_and_student_passed_in_all_subjects(subject_controller, subject_english, subject_science):
    graded_assignment = GradedAssignment('assignment', datetime(2001, 1, 1, 0, 0, 0, 1), 100, 60)

    subject_science.add_graded_assignment(graded_assignment)
    subject_english.add_graded_assignment(graded_assignment)

    subject_controller.add_subject(subject_english)
    subject_controller.add_subject(subject_science)

    filtered_subjects = subject_controller.filter_by_passing_grade(has_passing_grade=False)

    assert(len(filtered_subjects) == 0)

def test_should_return_subjects_which_study_time_goal_is_overdue(subject_controller, subject_english, subject_science):
    overdue_date = datetime(2000, 1, 1, 0, 0, 0, 0)

    valid_date = datetime.today() + timedelta(days=1)

    subject_science.set_time_study_goal(10, overdue_date)
    subject_english.set_time_study_goal(10, valid_date)

    subject_controller.add_subject(subject_science)
    subject_controller.add_subject(subject_english)

    filtered_subjects = subject_controller.filter_by_study_goal_overdue(True)

    assert(len(filtered_subjects) == 1)
    assert(subject_science in filtered_subjects.values())

def test_should_return_subjects_which_study_time_goal_is_not_overdue(subject_controller, subject_english, subject_science):
    overdue_date = datetime(2000, 1, 1, 0, 0, 0, 0)

    valid_date = datetime.today() + timedelta(days=1)

    subject_science.set_time_study_goal(10, overdue_date)
    subject_english.set_time_study_goal(10, valid_date)

    subject_controller.add_subject(subject_science)
    subject_controller.add_subject(subject_english)

    filtered_subjects = subject_controller.filter_by_study_goal_overdue(False)

    assert(len(filtered_subjects) == 1)
    assert(subject_english in filtered_subjects.values())

def test_should_return_empty_when_there_is_no_subject_with_study_time_goal_overdue(subject_controller, subject_english):
    valid_date = datetime.today() + timedelta(days=1)

    subject_english.set_time_study_goal(10, valid_date)

    subject_controller.add_subject(subject_english)

    filtered_subjects = subject_controller.filter_by_study_goal_overdue(True)

    assert(len(filtered_subjects) == 0)

def test_should_return_empty_when_all_subjects_study_time_goal_overdue(subject_controller, subject_english):
    overdue_date = datetime(2000, 1, 1, 0, 0, 0, 0)

    subject_english.set_time_study_goal(10, overdue_date)

    subject_controller.add_subject(subject_english)

    filtered_subjects = subject_controller.filter_by_study_goal_overdue(False)

    assert(len(filtered_subjects) == 0)

def test_calculate_average_term_grade_with_0_subjects(subject_controller):
    average_grade = subject_controller.get_average_term_grade()
    assert (average_grade == 0)


def test_calculate_average_term_grade_with_multiple_subjects(subject_controller):
    first_subject = Subject('first_subject', 100)
    second_subject = Subject('second_subject', 100)

    midterm_exam = GradedAssignment('midterm_exam', datetime.now(), 50, 25)
    simple_activity = GradedAssignment('simple_activity', datetime.now(), 10, 10)

    first_subject.add_graded_assignment(midterm_exam)
    first_subject.add_graded_assignment(simple_activity)

    second_subject.add_graded_assignment(midterm_exam)

    subject_controller.add_subject(first_subject)
    subject_controller.add_subject(second_subject)

    expected_result = (25 + (25 + 10)) / 2
    result = subject_controller.get_average_term_grade()

    assert(result == expected_result)

def test_get_total_credits_with_4_to_1_credit_conversion_method(subject_controller, subject_science, subject_english):
    subject_science.update_attendance(75)
    subject_english.update_attendance(38)

    subject_science.add_graded_assignment(GradedAssignment('Exam', datetime.now(), 100, 60))
    subject_english.add_graded_assignment(GradedAssignment('Exam', datetime.now(), 100, 60))

    subject_controller.add_subject(subject_science)
    subject_controller.add_subject(subject_english)
    
    expected_result = (subject_science.attendance.workload_hours + subject_english.attendance.workload_hours) / 4
    result = subject_controller.get_current_term_credits(credit_conversion_method = lambda x: x/4)

    assert(result == expected_result)

def test_total_credits_should_not_count_when_student_has_insufficient_attendance(subject_controller, subject_science):
    subject_science.add_graded_assignment(GradedAssignment('Exam', datetime.now(), 100, 60))
    subject_controller.add_subject(subject_science)
    
    assert(subject_controller.get_current_term_credits(credit_conversion_method = lambda x: x/4) == 0)

def test_total_credits_should_not_count_when_student_has_not_passing_grade(subject_controller, subject_science):
    subject_science.update_attendance(75)
    subject_controller.add_subject(subject_science)

    assert(subject_controller.get_current_term_credits(credit_conversion_method = lambda x: x/4) == 0)

def test_update_existing_subject_attendance(subject_controller, subject_english):
    subject_initial_attendance = subject_english.get_current_attendance()
    subject_controller.add_subject(subject_english)
    extra_attendance = 10
    subject_controller.update_subject_attendance(subject_english.name, extra_attendance)

    assert(subject_controller.subjects[subject_english.name].get_current_attendance() == subject_initial_attendance + extra_attendance)
