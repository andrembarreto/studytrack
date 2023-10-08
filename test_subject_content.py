from subject_content import SubjectContent
import json

def test_contents_should_be_considered_equals():
    first_content = SubjectContent('example_content_1', 1)
    second_content = SubjectContent('example_content_1', 2)
    first_content.mark_as_visited()
    
    assert(first_content == second_content)

def test_contents_should_be_considered_different():
    first_content = SubjectContent('example_content_1', 1)
    second_content = SubjectContent('example_content_2', 1)
    first_content.mark_as_visited()
    second_content.mark_as_visited()
    
    assert(not first_content == second_content)

def test_retrieve_unvisited_content_from_json_obj():
    original_content = SubjectContent('example_content', 1)
    
    retrieved_content = SubjectContent.from_json(original_content.to_json())
    
    assert(retrieved_content == original_content)

def test_retrieve_visited_content_from_json_obj():
    original_content = SubjectContent('example_content', 1)
    original_content.mark_as_visited()

    retrieved_content = SubjectContent.from_json(original_content.to_json())
    
    assert(retrieved_content == original_content)