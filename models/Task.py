from datetime import datetime
from typing import List
from models.Split import Split

class Task():
    def __init__(self):
        self.date = datetime.today()
        self.splits: List[Split] = []
        self.description: str = ''
    
    def add_split(self, s: Split) -> None:
        self.splits.append(s)
        
    def save_task(self):
        pass