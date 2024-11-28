import pytest
from task_manager import TaskManager


@pytest.fixture
def setup_task_manager():
    tasks = [
        {
            "id": 100,
            "title": "Test Task 1",
            "description": "Description 1",
            "category": "Category 1",
            "due_date": "2023-10-31",
            "priority": "высокий",
            "status": "Не выполнена"
        },
        {
            "id": 101,
            "title": "Test Task 2",
            "description": "Description 2",
            "category": "Category 2",
            "due_date": "2023-10-31",
            "priority": "средний",
            "status": "Не выполнена"
        },
    ]
    return TaskManager(tasks)


def test_add_task(setup_task_manager):
    setup_task_manager.add_task("Test Task 3", "Description 3", "Category 3", "2023-10-31", "низкий")
    assert len(setup_task_manager.tasks) == 3
    assert setup_task_manager.tasks[2].title == "Test Task 3"


def test_add_task(setup_task_manager):
    setup_task_manager.view_tasks()
    assert len(setup_task_manager.tasks) == 2


def test_status_task(setup_task_manager):
    setup_task_manager.status_task(102)
    assert setup_task_manager.tasks[0].status == "Выполнена"
    setup_task_manager.status_task(102)
    assert setup_task_manager.tasks[0].status == "Не выполнена"


def test_delete_task(setup_task_manager):
    setup_task_manager.delete_task(105)
    assert len(setup_task_manager.tasks) == 1


def test_search_tasks(setup_task_manager):
    assert setup_task_manager.search_tasks("1")[0].title == "Test Task 1"


def test_update_task(setup_task_manager, monkeypatch):
    field = "заголовок"
    new_title = "100"
    answers = iter([field, new_title])
    monkeypatch.setattr('builtins.input', lambda name: next(answers))
    setup_task_manager.update_task(108)
    assert setup_task_manager.tasks[0].title == "100"
