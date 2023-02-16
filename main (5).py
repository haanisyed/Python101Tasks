'''
This program's purpose is to examine the guestList (dictionary data structure) provided representing the holiday party at Vic Hall
and the guests list as well as the foods associated per person and the number of guests.
Date: December 2022
'''
#dictionary (main data structure)
guestList = {"Raisa": ["pizza", "cookies", 3], "Susan": ["salad", 2], "Jia": ["ice cream", 0], "Val": ["cake", 2],
                 "Brian": ["pasta", "cheese", "crackers", 2], "Chandra": ["burgers", "buns", 3]}

def print_guestList():
    names = guestList.keys() #the names of the guests (keys)
    for name in names: #for loop for name and associated food items
        print(name, 'is bringing', end = '')
        for i in range(0, len(guestList[name] - 1)):
            print(guestList[name][i], end = '')

def print_guests_attending_party(guestList): #i was not able to get this function to completely run. However this is what
    #i got to so far please accept my efforts.
    #aims at printing total num of guests attending party.
    the_new_guests = [] #initialize empty list
    for guest in guestList: #from my understanding we must use a for loop
        the_new_guests = guestList[name][-1] #the new guests
        total_people_coming = total_people_coming + the_new_guests #appends the total people coming and new guests arriving
    print("the total number of guests is", total_people_coming) #prints the total number of guests


def powley_list_of_people(guestlist, powleyGuests):
    '''
    This function returns list of names of people in 'powleyGuests' but not in 'guestList'
    :param guest_list: the variable for dictionary for original guests and their food items and number of guests being brought
    :param powleyGuests: the variable for list of powleyGuests
    :return: list of names of people in 'powleyGuests' but not in 'guestList'
    '''
    list_of_names = [] #will be returned. The list of names in powleyGuests but not in guestList
    for name in powleyGuests:
        if powleyGuests not in guestList: #if they are in powleyGuests but not in the guestList
            list_of_names.append(name) #
    return list_of_names #list of names in powleyGuests but not in guestList returned

def name_each_guest(names): #adds name of each powleyGuest not in original guest list to guestList
    #food item: 'tbd', additional guests: 0 list index. Then prints the dictionary showing all guests on guest list
    #+ food item they bringing
    for name in names:
        guestList.update({name: ['tbd', 0]}) #updates guestList so that the food item is 'tbd' and additional guests '0'
        for name in names:
            print(name, 'is bringing', end = '')
            for i in range(0, len(guestList[name]) - 1):
                print(guestList[name][i], end = '')


def list_food_items_num_guests(party_info):
    if party_info[2] > 0: #
        if len(party_info[0]) > 3 or party_info[0][0] == 'p':
            return True
    elif party_info[2] == 0:
        contains_s = False
        contains_p = False
        for element in party_info:
            for letter in element:
                if letter == 'p':
                    contains_p = True #if there is a letter P it will be true
                elif letter == 's': #if there is a S it will be true
                    contains_s = True
            if contains_s and contains_p:
                return True #if both return True
    return False #else returns false


def user_add_names_powleyGuests(powleyGuests):
    names_num = int(input('how many names would you like to add?: ')) #adds number of users based on user input
    for i in range(names_num): #for i in range loop
        name = input(f"Enter the name #{i+1}") #
        while powleyGuests.count(name) > 1:
          name = input('Sorry but that particular name exists already. Enter another please: ')
        powleyGuests.append(name)

def main(): #serves as a call to the remaining functions
    guestList = {"Raisa": ["pizza", "cookies", 3], "Susan": ["salad", 2], "Jia": ["ice cream", 0], "Val": ["cake", 2],
                 "Brian": ["pasta", "cheese", "crackers", 2], "Chandra": ["burgers", "buns", 3]}
    powleyGuests = ['Isla', 'Susan', 'Ellen', 'Jia', 'Raisa', 'Chandra', 'Wendy'] #reference to powleyGuests list
    names = powley_list_of_people(guestList, powleyGuests) #variable for return of powley_list_of people used in other functions
    party_info = print_guests_attending_party(guestList) #party_info variable used in list_food_items_num_guests function
    print_guestList() #call to first function
    print_guests_attending_party(guestList) #call to second function
    powley_list_of_people(guestList, powleyGuests) #call to third function
    name_each_guest(names) #call to fourth function
    list_food_item_num_guests(party_info) #call to fifth and final function


main()