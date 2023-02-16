"""
This program reads the data from a website into a dictionary(key:orderID, value(list): food item and price)
Date: December 2022
"""
import urllib.request
import string

def read_tim_hortons(url):#basing off of A9 suggestion
    '''
    The purpose of this function is to read the tim hortons website url into a dictionary that can be used by the task functions.
    :param url: the parameter in this function is the url website.
    :return: the return is the dictionary containing the data from the website.
    '''
    dict = {}
    try:
        response = urllib.request.urlopen(url) #makes the connection
        data = response.readline().decode('utf-8') #reads one line of data into the string
        data_length = len(data)
        the_orders = data[:data_length-1]
        while len(data)!= 0: #reads to the end of the website
            the_order = the_orders.split()
            itemName = ""
            for i in range(1, len(the_order)-1):
                itemName += " " + the_order[i]
            dict.update({the_order[0]: {'itemName': itemName, 'price': the_order[-1]}})
            data = response.readline().decode('utf-8')
            data_length = len(data)
            the_orders = data[:data_length - 1]
    except: #in the case that there is an error in reading the website into a dictionary
        print('404 Error. Something went wrong in accessing this URL ')
        return {} #returns an empty dictionary
    return dict #returns the dictionary with the data from the website



def lookup_order(the_orders):
    '''
    The purpose of this function is to fulfill choice#1 from menu of looking up the orderID's details (itemName and price).
    :param the_orders: the parameter is the_orders (reference to dictionary containing the data).
    :return: the return is the dictionary's values at the users_id entered by the user.
    '''
    users_id = input('Enter desired order ID (from 101 to 108) to view item name and price: ')
    while 101 > int(users_id) and int(users_id) > 108:
        print('The choice entered is invalid and not on menu. Please try again')
    if users_id in the_orders:
        print('the item name for the order id', users_id, 'is:')
        for i in range(len(the_orders[users_id]['itemName'])):
            print(the_orders[users_id]['itemName'][i], end=" ")
    print('the price for this order id is', the_orders[users_id]['price'])

    return the_orders[users_id]

def change_food_items(the_orders):
    '''
    the purpose of this function is to fulfill choice#2 from menu of changing the itemNames based on user input.
    :param the_orders: the parameter is the_orders (reference to dictionary containing the data).
    :return: none
    '''
    users_id = str(input('Enter desired order ID: '))
    print('The current items', users_id, 'are: ')
    for i in range(len(the_orders[users_id][0])):
        print(the_orders[users_id][0][i])
    print('What do you want to change the food items to?: ')
    for i in range(len(the_orders[users_id][0])): #for loop so program knows amount of items
        new_order_item = input('Enter new item: ') #will be present and can know the amount to change
        the_orders[users_id][0][i] = new_order_item
    print('The new items', users_id, 'are: ')
    for i in range(len(the_orders[users_id][0])):
        print(the_orders[users_id][0][i])

def donut_orders(the_orders):
    '''
    the purpose of this function is to fulfill choice#3 from menu of printing the orders containing donuts.
    :param the_orders: the parameter is the_orders (reference to dictionary containing the data).
    :return: none. Will print out the items containing donuts.
    '''
    for x in the_orders:
        if 'donut' in the_orders[x]['itemName']:
            print(x)

def remove_order(the_orders):
    '''
    the purpose of this function is to fulfill choice#4 from menu of removing the order from orderlist, when given orderid.
    :param the_orders: the parameter is the_orders (reference to dictionary containing the data).
    :return: will output the orderlist with removed key that was inputted by user.
    '''
    users_id = int(input('Enter desired order ID: '))
    if 101 <= users_id <= 110:
        order = the_orders.pop(users_id)
        return order



def total_not_donuts(the_orders):
    '''
    the purpose of this function is to fulfill choice#5 from menu of creating the total for not donut items.
    :param the_orders: the parameter is the_orders (reference to dictionary containing the data).
    :return: will return the total value.
    '''
    total = 0
    for key in the_orders.keys():
        if 'Donut' not in the_orders[key]['itemName']:
            total += float(the_orders[key]['price'])
            print(total)
    return total

def main():
    '''
    the purpose of this function is to serve as where the menu is that starts the program, and serves as a centre for calling functions.
    :return: no direct return. If the user enters a choice for a function that has a return, there will be a return.
    '''
    url = 'https://research.cs.queensu.ca/home/cords2/timHortons.txt'
    data = read_tim_hortons('https://research.cs.queensu.ca/home/cords2/timHortons.txt')
    the_orders = read_tim_hortons(url) #this will read the orders from the url
    response_of_user = input('Would you like a task to be completed. Enter yes or no: ')
    if response_of_user == 'yes':
            menu_choice = int(input('"Please choose one of the following actions:\n \
              1. Look up an order id and print the associated food and price.\n \
              2. allow a user to change food items for particular id.\n \
              3. print orders that have donut.\n \
              4. given the order id, remove order from order list.\n \
              5. calculate the total price of all orders that do not have donut.\n \
              6. Exit\n"))'))
            while menu_choice < 1 and menu_choice > 6:
                menu_choice = int(input('Please enter a number corresponding to a command between numbers 1 and 6: '))
            if menu_choice == 1:
                lookup_order(the_orders)
            elif menu_choice == 2:
                change_food_items(the_orders)
            elif menu_choice == 3:
                donut_orders(the_orders)
            elif menu_choice == 4:
                remove_order(the_orders)
            elif menu_choice == 5:
                total_not_donuts(the_orders)

main()
