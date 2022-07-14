# Julia Gordon
# 6/10/21
# Programming Assignment 2

# Defining my two lists:
table_order = ["Meatball Sub","Italian Sub","Pasta Salad","Liter Coke","Chips"]
menu_prices = [7.50,8.50,6.75,2.99,1.50]

# The heading: 
print("-------------------")
print("The Best Deli Ever!")
print("-------------------")

# Menu item and price on one line:
for index in range(len(table_order)):
	print(table_order[index], "- $", menu_prices[index])
print("-------------------")

# The total:
total = sum(menu_prices)
print(f"Total:","$",round(total,2))  

# The tax: 
tax_percent = 6.75
tax = total*(tax_percent/100)
print(f"Tax",tax_percent,"%:","$",round(tax,2))

# The grand total:
grand_total = total+tax
print(f"Grand Total:","$",round(grand_total,2))

# The goodbye message:
print("-------------------")
print("THANK YOU FOR YOUR BUSINESS!")
print("-------------------")

