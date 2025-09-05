#This class will be handling the Budget part of the application

from datetime import date, timedelta

class Budget: 

    def __init__(self):
        self.start_date = date.today()
        self.end_date = self.start_date + timedelta(days=6)
        self.categories = []
        self.available = 0

    
    def get_start_Date(self):
        return self.start_date
    
    def get_end_date(self):
        return self.end_date
    
    def add_category(self, newCategory):
        self.categories.append(newCategory)

    def increase_budget(self, amount):
         self.available +=  amount

    def get_budget(self):
        return self.available
