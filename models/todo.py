from datetime import datetime

class Todo:
    def __init__(self, title: str, details: str, created_at: str = None):
        self.title = title
        self.details = details
        self.created_at = created_at or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
