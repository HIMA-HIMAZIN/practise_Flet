from datetime import datetime

class Todo:
    def __init__(self, title: str, details: str, status: bool = False, created_at: str = None):
        self.title = title
        self.details = details
        self.status = status
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
