"""
This program calculates the subtotal, sales tax, and final total of four items bought from the Retail store
Date: Sept 2022
"""
#The cost of item one can be entered below 
item1_cost = float(input("Enter the cost of item one: "))
#The cost of item two can be entered below
item2_cost = float(input("Enter the cost of item two: "))
#The cost of item three can be entered below
item3_cost = float(input("Enter the cost of item three: "))
#The cost of item four can be entered below
item4_cost = float(input("Enter the cost of item four: "))
#The line below states thirteen percent, the tax assigned in the question, in the form of a decimal for calculation purposes
tax_percentage = 0.13
#The calculation for the subtotal is shown below. The subtotal is the addition of all the items before tax is included.
items_subtotal = (float(item1_cost) + float(item2_cost) + float(item3_cost) + float(item4_cost))
#The line below calculates the amount of tax that will be charged by multiplying 0.13 (the 13% sales tax) with the subtotal
salestax_total = (float(items_subtotal) * float(tax_percentage))
#The line below calculates the final total by addition of subtotal and tax charged
final_total = (float(items_subtotal) + float(salestax_total))
#The final line concludes by stating the subtotal, tax charged, and final total
final_statement = input("The subtotal is $" + str(items_subtotal) + ",the sales tax is $" + str(salestax_total) + ",the final cost is $" + str(final_total))
