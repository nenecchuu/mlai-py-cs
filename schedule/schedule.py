import datetime

class Schedule():

    def __init__(self):
        self.name = ''
        self.date = datetime.datetime.now()

    def withName(self, name: str):
        self.name = name
        return self

    def withDate(self, date: datetime.datetime): 
        self.date = date
        return self
    