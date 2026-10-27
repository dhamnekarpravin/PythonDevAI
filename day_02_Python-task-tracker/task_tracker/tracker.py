from task_tracker.models import Task


class TaskTracker:
    def __init__(self):
        self.tasks: list[Task] = []

    def add_task(self, title: str) -> Task:
        if not title.strip():
            raise ValueError("Task title cannot be empty.")

        task = Task(title=title.strip())
        self.tasks.append(task)
        return task

    def get_task(self, task_number: int) -> Task:
        if task_number < 1 or task_number > len(self.tasks):
            raise IndexError("Invalid task number.")

        return self.tasks[task_number - 1]

    def complete_task(self, task_number: int) -> Task:
        task = self.get_task(task_number)
        task.mark_complete()
        return task

    def delete_task(self, task_number: int) -> Task:
        task = self.get_task(task_number)
        self.tasks.remove(task)
        return task

    def view_tasks(self) -> str:
        if not self.tasks:
            return "No tasks yet."

        lines = ["Your Tasks:"]
        for number, task in enumerate(self.tasks, start=1):
            lines.append(task.display(number))

        return "\n".join(lines)