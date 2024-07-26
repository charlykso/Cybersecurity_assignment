import datetime
import uuid

class SchoolBase:
    def __init__(self, name, email) -> None:
        self.id = uuid.uuid4()
        self.name = name
        self.email = email
        self.created_at = datetime.datetime.now()
    
    def getId(self):
        return self.id
    
    def getName(self):
        return self.name
    
    def __str__(self) -> str:
        return f"{self.id} {self.name} {self.email}"