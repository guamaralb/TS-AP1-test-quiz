import pytest
from model import Question


def test_create_question():
    question = Question(title='q1')
    assert question.id != None

def test_create_multiple_questions():
    question1 = Question(title='q1')
    question2 = Question(title='q2')
    assert question1.id != question2.id

def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title='')
    with pytest.raises(Exception):
        Question(title='a'*201)
    with pytest.raises(Exception):
        Question(title='a'*500)

def test_create_question_with_valid_points():
    question = Question(title='q1', points=1)
    assert question.points == 1
    question = Question(title='q1', points=100)
    assert question.points == 100

def test_create_choice():
    question = Question(title='q1')
    
    question.add_choice('a', False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == 'a'
    assert not choice.is_correct
    
##################### New tests
def test_new_add_correct_choice():
    new_question = Question('q1')
    
    c1 = new_question.add_choice('c1', True)
    
    assert c1.is_correct
    
def test_new_create_invalid_choice():
    new_question = Question('c1')
    
    with pytest.raises(Exception):
        new_question.add_choice('')
    with pytest.raises(Exception):
        new_question.add_choice('a'*101)
    
def test_new_create_question_with_invalid_points():
    with pytest.raises(Exception):
        Question('q1', points=-1)
    with pytest.raises(Exception):
        Question('q1', points=101)
        
def test_new_remove_choice():
    new_question = Question('q1')
    
    choice = new_question.add_choice('c1')
    
    assert len(new_question.choices) == 1
    
    new_question.remove_choice_by_id(choice.id)
    
    assert len(new_question.choices) == 0
    
def test_new_remove_invalid_choice():
    new_question = Question('q1')
    
    new_question.add_choice('c1')
    
    assert len(new_question.choices) == 1
    
    with pytest.raises(Exception):
        new_question.remove_choice_by_id(-1)
    
def test_new_remove_all_choices():
    new_question = Question('q1')
    
    new_question.add_choice('c1')
    new_question.add_choice('c2')
    
    assert len(new_question.choices) == 2
    
    new_question.remove_all_choices()
    
    assert len(new_question.choices) == 0
    
def test_new_set_correct_choices():
    new_question = Question('q1')
    
    c1 = new_question.add_choice('c1')
    c2 = new_question.add_choice('c2')
    new_question.add_choice('c3')
    
    new_question.set_correct_choices([c1.id, c2.id])

def test_new_set_invalid_correct_choices():
    new_question = Question('q1')
    
    new_question.add_choice('c1')
    new_question.add_choice('c2')
    new_question.add_choice('c3')
    
    with pytest.raises(Exception):
        new_question.set_correct_choices([-1])

def test_new_select_correct_choice():
    new_question = Question('q1')
    
    c1 = new_question.add_choice('c1')
    new_question.add_choice('c2')
    new_question.add_choice('c3')
    
    new_question.set_correct_choices([c1.id])
    
    correct_choices = new_question.correct_selected_choices([c1.id])
    
    assert correct_choices == [c1.id]
    
def test_new_select_more_than_max_choices():
    new_question = Question('q1')
    
    c1 = new_question.add_choice('c1')
    c2 = new_question.add_choice('c2')
    new_question.add_choice('c3')
    
    new_question.set_correct_choices([c1.id])
    
    with pytest.raises(Exception):
        new_question.correct_selected_choices([c1.id, c2.id])
