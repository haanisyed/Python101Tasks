"""
This program calculates the cost for ordering a meal at a restaurant including the tip as an amount and the tax.
Date: Sept 2022
"""
#the line below represents the begenning of the menu and says the sentence "Items available for purchase"
print(input('Items available for purchase'))
#the line below represents the item 1 being the chicken wrap costing $4.50 
print(input('1. Chicken Wrap $4.50'))
#the line below represents the item 2 being the 10 wings meal costing $16.99
print(input('2. Wings (10) $16.99'))
#the line below represents the item 3 being the fries costing $4.59
print(input('3. Fries $4.59'))
#the line below represents the item 4 being the Meatball sub costing $8.39
print(input('4. Meatball sub $8.39'))
#the line below represents the item 5 being the soup costing $2.95
print(input('5. Soup $2.95'))
#the line below asks the user to enter a number from 1-5 in the menu to mention the item they would like to purchase
number_purchase = int(input('Enter the number corresponding to the item that you would like to purchase: '))
#if the user enters a number that is not equal to and above 1 but equal to and below 5 at the previous line: there will be an error saying 'Invalid Response' 
if not 1 <= number_purchase <= 5:
#as mentioned in the last hashtag, the program would print 'Invalid response' in that scenario
    print('Invalid response')
#if the user enters a number that is equal to and above 1 but equal to and below 5: the following if and elif statements with the prices of the respective items will run
if 1 <= number_purchase <=5:
#the line below states that if the user enters 1: the price will be $4.50 (before tip and tax)
    if number_purchase == 1:
        price = 4.50
#the line below states that if the user enters 2: the price will be $16.99 (before tip and tax)
    elif number_purchase == 2:
        price = 16.99
#the line below states that if the user enters 3: the price will be $4.59 (before tip and tax)
    elif number_purchase == 3:
        price = 4.59
#the line below states that if the user enters 4: the price will be $8.39 (before tip and tax)
    elif number_purchase == 4:
        price = 8.39
#the line below states that if the user enters 5: the price will be $2.95 (before tip and tax)
    elif number_purchase == 5:
        price = 2.95
#the line below aks the user if they would like to tip. If the user answers no, and they are prompted to still enter a tip value: they should enter "0" as the value
tip_question = (input('Would you like to tip?: '))
#the line below helps to set up for the tip amount which is used in the final total calculations
if tip_question == 'yes' or 'no':
#the line below asks whether the tip value to be entered is percentage or amount
    print(input('percentage or amount: '))
#the line below asks to enter the exact real tip amount to maximize possible efficiency
    tip = (float(input('Enter tip amount: ')))
#else statement below to fulfill the if-elif-else sequence
else:
    print('invalid')
#the tax percentage mentioned in the question is 5% which is mentioned in decimal form below so it can be used in the final total calculations efficiently
tax_percentage = 0.05
#the final total calculation involving item cost + tip + tax is mentioned below
final_total = ((float(price) * float(tax_percentage)) + float(price) + float(tip))
#the line below states the final total in the form of a sentence
print(input("the final cost is $" + str(final_total)))
