from dataclasses import dataclass, field


@dataclass
class Task:
    title: str
    completed: bool = False
    tags: list[str] = field(default_factory=list)

    def mark_complete(self):
        self.completed = True

    def mark_pending(self):
        self.completed = False

    def display(self, number: int) -> str:
        status = "Done" if self.completed else "Pending"
        return f"{number}. {self.title} - {status}"