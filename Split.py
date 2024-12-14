from datetime import datetime

class Split():
    def __init__(self):
        self.date = datetime.today()
        self.start_time = datetime.now()
        self.end_time = None
        
    def complete(self):
        self.end_time = datetime.now()