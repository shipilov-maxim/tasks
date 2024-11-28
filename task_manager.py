from typing import List, Dict, Union

from task import Task
from validators import get_valid_input, get_valid_input_date


class TaskManager:

    def __init__(self, tasks: List[Dict]) -> None:
        tasks_list = []
        for task in tasks:
            try:
                tasks_list.append(
                    Task(
                        task_id=task['id'],
                        title=task['title'],
                        description=task['description'],
                        category=task['category'],
                        due_date=task['due_date'],
                        priority=task['priority'],
                        status=task['status']
                    )
                )
            except ValueError as e:
                print(f"Некорректные данные в задаче №{task['id']}: {e}\nПроверьте data.json")
                exit()
        self.tasks: List[Task] = tasks_list

    def add_task(self, title: str, description: str, category: str, due_date: str, priority: str) -> None:
        task_id = len(self.tasks) + 1
        task = Task(task_id, title, description, category, due_date, priority)
        self.tasks.append(task)
        print(f"Задача добавлена: {title}")

    def view_tasks(self, category: str = None) -> List[Task]:
        filtered_tasks = [task for task in self.tasks if category is None or task.category == category]
        if len(filtered_tasks) == 0:
            print("Задач нет")
        else:
            for task in filtered_tasks:
                print(task)
            return filtered_tasks

    def update_task(self, task_id: int) -> None:

        for task in self.tasks:
            if task.id == task_id:
                print("Выбранная задача:\n", task)

                while True:
                    choice = get_valid_input(
                        "Что вы хотели бы отредактировать? (заголовок, описание, срок, приоритет): "
                    ).lower()

                    if choice == "заголовок":
                        new_title = get_valid_input("Введите новый заголовок: ")
                        task.title = new_title
                        print("Заголовок задачи успешно обновлен.")
                        break
                    elif choice == "описание":
                        new_description = get_valid_input("Введите новое описание: ")
                        task.description = new_description
                        print("Описание задачи успешно обновлено.")
                        break
                    elif choice == "срок":
                        new_due_date = get_valid_input_date()
                        task.due_date = str(new_due_date)
                        print("Срок задачи успешно обновлен.")
                        break
                    elif choice == "приоритет":
                        new_priority = get_valid_input("Введите новый приоритет (низкий, средний, высокий): ",
                                                       valid_choices=['низкий', 'средний', 'высокий'])
                        task.priority = new_priority
                        print("Приоритет задачи успешно обновлен.")
                        break
                    elif choice == "статус":
                        new_status = get_valid_input("Введите новый статус (Выполнена, Не выполнена): ",
                                                     valid_choices=['Выполнена', 'Не выполнена'])
                        task.status = new_status
                        print("Статус задачи успешно обновлен.")
                        break
                    else:
                        print("Некорректный выбор. Пожалуйста, выберите заголовок, описание, срок или приоритет.")
                        continue

    def status_task(self, task_id: int) -> None:
        print(self.tasks)
        for task in self.tasks:
            if task.id == task_id:
                if task.status == "Выполнена":
                    task.status = "Не выполнена"
                    print(f"Задача {task_id} отмечена как невыполненная.")
                elif task.status == "Не выполнена":
                    task.status = "Выполнена"
                    print(f"Задача {task_id} отмечена как выполненная.")
                return
            else:
                print("Задача не найдена.")

    def delete_task(self, task_id: int) -> None:
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        if len(self.tasks) < initial_count:
            print(f"Задача {task_id} удалена.")
        else:
            print("Задача не найдена.")

    def search_tasks(self, keyword: str) -> List[Task]:
        found_tasks = [task for task in self.tasks if
                       keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]
        for task in found_tasks:
            print(task)
        return found_tasks

    def get_all_tasks(self) -> List[Dict[str, Union[int, str]]]:
        return [task.to_dict() for task in self.tasks]
