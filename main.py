import json
import os

from task_manager import TaskManager
from validators import get_valid_input, get_valid_input_date

FILE_PATH = 'data.json'


def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    return []


def save_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def main():
    tasks = load_data(FILE_PATH)
    task_manager = TaskManager(tasks)

    while True:
        command = get_valid_input("Введите команду (add/view/update/delete/search/exit): ",
                                  valid_choices=['add', 'view', 'update', 'delete', 'search', 'exit'])

        if command == 'add':
            title = get_valid_input("Введите название задачи: ")
            description = get_valid_input("Введите описание задачи: ")
            category = get_valid_input("Введите категорию задачи: ")
            due_date = get_valid_input_date()
            priority = get_valid_input("Введите приоритет (низкий, средний, высокий): ",
                                       valid_choices=['низкий', 'средний', 'высокий'])
            task_manager.add_task(title, description, category, due_date, priority)

        elif command == 'view':
            category = input("Введите категорию для просмотра (оставьте пустым для всех): ")
            task_manager.view_tasks(category or None)

        elif command == 'update':
            try:
                task_id = int(input("Введите ID задачи для обновления: "))
                task_manager.update_task(task_id)
            except ValueError:
                print("Пожалуйста, введите корректный номер задачи.")

        elif command == 'delete':
            try:
                task_id = int(input("Введите ID задачи для удаления: "))
                task_manager.delete_task(task_id)
            except ValueError:
                print("Пожалуйста, введите корректный номер задачи.")

        elif command == 'search':
            keyword = input("Введите ключевое слово для поиска: ")
            task_manager.search_tasks(keyword)

        elif command == 'exit':
            save_data(FILE_PATH, task_manager.get_all_tasks())
            break


if __name__ == "__main__":
    main()
