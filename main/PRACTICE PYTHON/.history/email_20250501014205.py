import re
from dattetime import date

class user:
    def __init__(self,name,email,intrest):
        self.name=name
        self.email=email
        self.interest=interest
        self.date=date.today()

    def is_valid_email