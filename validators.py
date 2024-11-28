from datetime import datetime, date
from typing import List


def validate_id(new_id: int, existing_ids: set) -> tuple:
    """
    Проверяет уникальность идентификатора. Если не уникальный,
    увеличиваем id.
    """
    while new_id in existing_ids:
        new_id += 1
    existing_ids.add(new_id)
    return new_id, existing_ids


def validate_date(due_date: str) -> date:
    try:
        return datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Неверный формат даты. Используйте YYYY-MM-DD.")


def validate_priority(priority: str) -> str:
    valid_priorities = ['низкий', 'средний', 'высокий']
    if priority.lower() not in valid_priorities:
        raise ValueError(f"Приоритет должен быть одним из: {', '.join(valid_priorities)}")
    return priority


def validate_status(status: str) -> str:
    valid_status = ['Не выполнена', 'Выполнена']
    if status not in valid_status:
        raise ValueError(f"Статус должен быть одним из: {', '.join(valid_status)}")
    return status


def get_valid_input(prompt: str, valid_choices: List[str] = None) -> str:
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == '':
            print("Пожалуйста, введите значение")
        elif valid_choices and user_input not in valid_choices:
            print(f"Пожалуйста, выберите один вариант из: {', '.join(valid_choices)}")
        else:
            return user_input


def get_valid_input_id(prompt: str) -> int:
    while True:
        try:
            task_id = int(input(prompt))
            if task_id == '':
                print("Пожалуйста, введите значение")
            else:
                return task_id
        except ValueError:
            print("Пожалуйста, введите корректный номер задачи.")


def get_valid_input_date() -> str:
    while True:
        due_date = input("Введите срок выполнения (YYYY-MM-DD): ")
        try:
            if validate_date(due_date) >= date.today():
                return due_date
            else:
                print("Дата не должна быть в прошедшем времени")
        except ValueError as e:
            print(e)
