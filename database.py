# Julia Gordon
# 7/23/21
# Assignment 5:
    # database class code:

# The database class will need the following data:
    # 1. A list of suppliers
# The database class will need the following methods:
    # 1. An init method to initialize the database
    # 2. A method to add a supplier
    # 3. A method to find the lowest cost for a part. The input will be a part name, and the output will be two values: the name of the supplier, and the cost. If the part is not sold by any suppliers, returnFalse, False.

class Database:
    def __init__(self):
         self.suppliers = []
  
    def add_supplier(self, supp):
        self.suppliers.append({"supp": supp})

    def find_part(self, name):    ### I know this is wrong
        minimum = min(self.suppliers)
        s = None
        for supp in self.suppliers:
            if supp.isSupplied(name):
                cost = supp.cost(name)
            if cost < minimum:
                minimum = cost
                s = supp
            if s is not None:
                return s.name, cost
            else:
                return False
