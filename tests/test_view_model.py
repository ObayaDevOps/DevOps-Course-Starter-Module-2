from todo_app.view_model import ViewModel
import pytest

# fixture for tests set up
@pytest.fixture
def on_test_start():
    print("Here before tests")

def test_show_todo_items():
    result = ViewModel.show_todo_items()
    for item in result.items:
        assert item.status == 'To Do'

def test_show_todo_items():
    result = ViewModel.show_doing_items()
    for item in result.items:
        assert item.status == 'Doing'

def test_show_todo_items():
    result = ViewModel.show_done_items()
    for item in result.items:
        assert item.status == 'Completed'

def test_error():
    with pytest.raises(TypeError):
        'text' + 6