import pytest
from subject_controller import SubjectController, Subject

def test_should_be_able_to_add_subjects_with_different_names():
    controller = SubjectController()
    
    first_subject = Subject('science', 100)
    controller.add_subject(first_subject)
    assert(first_subject in controller.subjects_list)
    
    second_subject = Subject('english', 50)
    controller.add_subject(second_subject)
    assert(second_subject in controller.subjects_list)

def test_should_not_be_able_to_add_subject_with_repeated_name():
    controller = SubjectController()

    first_subject = Subject('science', 100)
    controller.add_subject(first_subject)

    second_subject = Subject('science', 50)
    with pytest.raises(ValueError):
        controller.add_subject(second_subject)

def test_can_remove_added_subject():
    controller = SubjectController()
    subject = Subject('software_engineering', 100)

    controller.add_subject(subject)
    assert(subject in controller.subjects_list)

    controller.remove_subject(subject)
    assert(subject not in controller.subjects_list)

def test_cannot_remove_subject_not_added():
    controller = SubjectController()
    subject = Subject('software_engineering', 100)

    with pytest.raises(ValueError):
        controller.remove_subject(subject)
