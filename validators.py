from datetime import datetime, date


def validate_date(due_date):
    try:
        return datetime.strptime(due_date, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError("Неверный формат даты. Используйте YYYY-MM-DD.")


def validate_priority(priority):
    valid_priorities = ['низкий', 'средний', 'высокий']
    if priority not in valid_priorities:
        raise ValueError(f"Приоритет должен быть одним из: {', '.join(valid_priorities)}")
    return priority


def validate_status(status):
    valid_status = ['Не выполнена', 'Выполнена']
    if status not in valid_status:
        raise ValueError(f"Статус должен быть одним из: {', '.join(valid_status)}")
    return status


def get_valid_input(prompt, valid_choices=None):
    while True:
        user_input = input(prompt).strip()
        if user_input == '':
            print("Пожалуйста, введите значение")
        elif valid_choices and user_input not in valid_choices:
            print(f"Пожалуйста, выберите один вариант из: {', '.join(valid_choices)}")
        else:
            return user_input


def get_valid_input_date():
    while True:
        due_date = input("Введите срок выполнения (YYYY-MM-DD): ")
        try:
            if validate_date(due_date) >= date.today():
                return due_date
            else:
                print("Дата не должна быть в прошедшем времени")
        except ValueError as e:
            print(e)
