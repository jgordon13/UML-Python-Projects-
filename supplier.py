# Julia Gordon
# 7/23/21
# Assignment 5:
    # supplier class code:

# The supplier class will need to contain the following information:
    # 1. The company name
    # 2. A list of the parts the company supplies
# The supplier class will need the following methods:
    # 1. An init method to set the company name
    # 2. A method that lets the user add a part to the list of parts a company supplies
    # 3. A method that takes a part argument and returns the cost of that part.
    # 4. A method that takes a part argument and returns a Boolean if the part is supplied by thecompany (True if it does, False if it does not).

class Supplier:
    def __init__(self,name):
        self.name = name
        self.parts = []

    def add_part(self, name, cost):
        self.parts.append({"name": name, "cost": cost})
  
    def find_cost(self, name):
        for p in self.parts:
            if p.name == name:
                return p.cost
  
    def isSupplied(self, name):
        for pa in self.parts:
            if name==pa.name:
                return True
            else:
                return False
