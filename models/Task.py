from datetime import datetime
from typing import List
from models.Split import Split

class Task():
    def __init__(self):
        self.date = datetime.today().strftime('%Y-%m-%d')
        self.splits: List[Split] = []
        self.description: str = ''
        self.hours = 0.0
    
    def add_split(self, s: Split) -> None:
        self.hours = (s.end_time - s.start_time).seconds / 60.0 / 60.0
        # self.splits.append({"start_time": s.start_time.strftime("%H:%M"), "end_time":s.end_time.strftime("%H:%M")})
        self.splits.append(s)
        
    def save_task(self):
        pass