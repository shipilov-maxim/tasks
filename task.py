from validators import validate_date, validate_priority, validate_status


class Task:
    def __init__(self, task_id, title, description, category, due_date, priority, status="Не выполнена"):
        self.id = task_id
        self.title = title
        self.description = description
        self.category = category
        self.due_date = validate_date(due_date)
        self.priority = validate_priority(priority)
        self.status = validate_status(status)

    def __str__(self):
        return f"""
            Id: {self.id},
            Название: {self.title},
            Описание: {self.description},
            Категория: {self.category},
            Срок выполнения: {self.due_date},
            Приоритет: {self.priority},
            Статус: {self.status}
        """

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": str(self.due_date),
            "priority": self.priority,
            "status": self.status
        }
