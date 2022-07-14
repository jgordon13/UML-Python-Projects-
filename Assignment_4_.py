# Julia Gordon
# 7/12/21
# Assignment 4:

#json string/dictionary
supplier_data = '{"parts": ["sprocket", "gizmo", "widget", "dodad"], "sprocket": {"price": 3.99, "quantity": 32}, "gizmo": {"price": 7.98, "quantity": 2}, "widget": {"price": 14.32, "quantity": 4}, "dodad": {"price": 0.5, "quantity": 0}}'


### Your code goes here

parts = ["sprocket", "gizmo", "widget", "dodad"]
quanity = [32, 2, 4, 0]
prices = {'sprocket': 3.99,'gizmo': 7.98, 'widget': 14.32, 'dodad': 0.50} 
inventory = {'sprocket': 32, 'gizmo': 2, 'widget': 4, 'dodad': 0}
    
print("Welcome to the parts ordering system, please enter in a part name, followed by a quantity")
print()
print()
print("Parts for order are:")
print()
for key in inventory:
    print(key)
print()
print()

# this needs to be in a while loop
    # part quanity can only be asked for if the user enters a valid part
    # part can only be uses if they are in the given amount
    
    # use a dictionary and a tupple to make the 'my_order" for the second loop
    
order = {}
while True:  
    # This code is for user validations:
    
    part_name = input("Please enter in a part name, or quit to exit: ").lower()
    print()
    if part_name == 'quit':    # customer can exit the loop
        break
    
    if part_name not in supplier_data:    #Lets the customer know if they entered an unknow part
        print("ERROR - part does not exist, try again.")
        print()
        continue
    
    if part_name == "sprocket" or "Sprocket" or "SPROCKET":    #customer wants to get a sprocket
        order['sprocket']=int(input("Please enter a quantity to order: "))
        print()
        if int(order['sprocket']) > inventory['sprocket']:
            print('ERROR - only ', inventory['sprocket'], 'sprockets are avalible!')
            print()
            continue
        else: # that will subtract the quantity of the order from the inventory
            inventory['sprocket'] = inventory['sprocket'] - order['sprocket']
            continue
    if part_name == "gizmo" or "Gizmo" or "GIZMO":    #customer wants to buy a gizmo 
        order['gizmo']=int(input("Please enter a quantity to order: "))
        print()
        if int(order['gizmo']) > inventory['gizmo']:
            print('ERROR - only ', inventory['gizmo'], 'gizmos are avalible!')
            print()
        else: # that will subtract the quantity of the order from the inventory
            inventory['gizmo'] = inventory['gizmo'] - order['gizmo']
            continue 
    if part_name == "widget" or "Widget" or "WIDGET":    #customer wants to buy a widget   
        order['widget']=int(input("Please enter a quantity to order: "))
        print()
        if int(order['widget']) > inventory['widget']:
            print('ERROR - only ', inventory['widget'],' widgets are avalible!')
            print()
        else: # that will subtract the quantity of the order from the inventory
            inventory['widget'] = inventory['widget'] - order['widget']
            continue
    if part_name == "dodad" or "Dodad" or "DODAD":    #customer wants to buy a dodad  
        order['dodad']=int(input("Please enter a quantity to order: "))
        print()
        if int(order['dodad']) > inventory['dodad']: 
            print("ERROR - no dodads are avalible!")
            print()
        else: # that will subtract the quantity of the order from the inventory
            inventory['dodad'] = inventory['dodad'] - order['dodad']
            continue
        
    
#order total:
    
print("Your order: ")
print()
# here it prints out what the customer ordered - the quanity of the part: 
for data in order.items():
    print(data[0],"-", data[1], end='')
# individual part totals and prices:    
total = 0
for item in prices:
    total = prices[item] + order[item]
    print(" @", prices[item], end='')
    print(" = ", round(total,2))

    
    
    
    
#order_total = 
#print("Total: ", order_total, '$')
print()
print("Thank you for using the parts ordering system!")


# TO DO -
    #1.) FIGURE OUT HOW TO GET THE PRICE IN THERE
    #2.) DO THE INDIVIDUAL TOTALS AND THE GRAND TOTAL FOR THE ORDER
  

