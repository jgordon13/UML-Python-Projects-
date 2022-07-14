# Julia Gordon
# 7/23/21
# Assignment 5:
    # part class code:

#The parts class will need to contain the following information:
    # 1. Part name
    # 2. Part cost
#The parts class will need to contain the following methods:
    #1. An init method that lets the user set the name and cost of the part

class Part:
    def __init__(self,name,cost):
        self.name = name
        self.cost = cost
