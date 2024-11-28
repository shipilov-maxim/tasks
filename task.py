from datetime import date
from typing import Dict, Union

from validators import validate_date, validate_priority, validate_status, validate_id


class Task:
    existing_ids = set()

    def __init__(self, task_id: int, title: str, description: str, category: str, due_date: str, priority: str,
                 status="Не выполнена") -> None:
        self.id, self.existing_ids = validate_id(task_id, self.existing_ids)
        self.title: str = title
        self.description: str = description
        self.category: str = category
        self.due_date: date = validate_date(due_date)
        self.priority: str = validate_priority(priority)
        self.status: str = validate_status(status)

    def __str__(self) -> str:
        return f"""
            Id: {self.id},
            Название: {self.title},
            Описание: {self.description},
            Категория: {self.category},
            Срок выполнения: {self.due_date},
            Приоритет: {self.priority},
            Статус: {self.status}
        """

    def to_dict(self) -> Dict[str, Union[int, str]]:
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "category": self.category,
            "due_date": str(self.due_date),
            "priority": self.priority,
            "status": self.status
        }
