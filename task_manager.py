from task import Task


class TaskManager:
    def __init__(self, tasks):
        tasks_list = []
        for task in tasks:
            try:
                tasks_list.append(Task(task_id=task['id'],
                                       title=task['title'],
                                       description=task['description'],
                                       category=task['category'],
                                       due_date=task['due_date'],
                                       priority=task['priority'],
                                       status=task['status', "Не выполнена"]))
            except ValueError as e:
                print(f"Некорректные данные в задаче №{task['id']}: {e}\nПроверьте data.json")
                exit()
        self.tasks = tasks_list

    def add_task(self, title, description, category, due_date, priority):
        task_id = len(self.tasks) + 1
        try:
            task = Task(task_id, title, description, category, due_date, priority)
            self.tasks.append(task)
            print(f"Задача добавлена: {title}")
        except ValueError as e:
            print(f"Ошибка при добавлении задачи: {e}")

    def view_tasks(self, category=None):
        filtered_tasks = [task for task in self.tasks if category is None or task.category == category]
        if len(filtered_tasks) == 0:
            print("Задач нет")
        else:
            for task in filtered_tasks:
                print(task)

    def update_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                task.status = "Выполнена"
                print(f"Задача {task_id} отмечена как выполненная.")
                return
        print("Задача не найдена.")

    def delete_task(self, task_id):
        initial_count = len(self.tasks)
        self.tasks = [task for task in self.tasks if task.id != task_id]
        if len(self.tasks) < initial_count:
            print(f"Задача {task_id} удалена.")
        else:
            print("Задача не найдена.")

    def search_tasks(self, keyword):
        found_tasks = [task for task in self.tasks if
                       keyword.lower() in task.title.lower() or keyword.lower() in task.description.lower()]
        for task in found_tasks:
            print(task)

    def get_all_tasks(self):
        return [task.to_dict() for task in self.tasks]
