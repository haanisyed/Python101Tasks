'''
The purpose of this program is to provide a bingo game experience to user. Items for bingo card will be selected at random from a list of items read from this website.
3X3 bingo card (using a list of lists where each sublist is a row in the card) by randomly choosing 9 items from the list of items read from the website.  There must be no duplicates.  
Date: Nov 2022
'''


import urllib.request
import random
url = 'https://research.cs.queensu.ca/home/cords2/zoombingo.txt' #making the url a string
response = urllib.request.urlopen(url)
data = response.readline().decode('utf-8')

def website_reading(url):
    '''
    the purpose of the website_reading() function is to connect and read the website with the lists and then return the list of items read from the website.
    :param url: the url serves as the parameter representing the url from which to read the data in the website reading function.
    :return: will return the exact list of items read from the website.
    '''
    website_list = [] #create an empty list to store the list of items
    str = "  "
    try:
        response = urllib.request.urlopen(url) #open the connection to the website
    except:
        print('404 Error: The requested url could not be found unfortunately. That is all we know')
        return []
    data = response.readline().decode('utf-8')
    while len(data) != 0:
        str += data # add this string to the list of items
        data = response.readline().decode('utf-8')
    website_list = str.split('\n') #remove the end of line character from this string
    return website_list #return the list of items read from website




def bingo_card_creation(website_list):
    '''
    The purpose of the bingo_card_creation() function is to create the 3by3 list for the bingo card also known as the bingo card creation.
    :param website_list: the parameter website_list refers to the list of items read from the website.
    :return: the return of this function is the official list for the sublists.
    '''
    list_for_sublists = []
    website_listtmp = website_list.copy()
    for j in range(0,3):
        the_row = []
        for i in range(0,3):
            sample_bingo_card = random.choice(website_listtmp)
            website_listtmp.remove(sample_bingo_card)
            the_row.append(sample_bingo_card)
        list_for_sublists.append(sample_bingo_card)

    return list_for_sublists




def print_bingo_card(list_for_sublists):
    '''
    This function's purpose is to take the parameter and print the bingo card that was created in the previous function.
    :param list_for_subtitles: the parameter refers to the bingoCard being examined and to be printed.
    :return: no exact official return with a return part in the function, it will print the 'bingo card' however
    '''
    the_row = []
    i = 1
    for the_row in list_for_sublists:
        for item in the_row:
            if i % 3 != 0:
                print(item, '|| ', end = '')
            else:
                print(item, end = '')
            i += 1
        print()




def play(bingoCard, website_list):
    '''
    This function's purpose is to officially play the game: user is asked for input and based on their response: either game ends, they win or asked to play again.
    :param all_data: the all_data parameter represents the Dataset
    :param bingoCard: represents the value attained in the function of bingo card creation
    :return:
    '''
    card_display = bingoCard[0][0:], bingoCard[1][0:], bingoCard[2][0:]
    for i in card_display:
        print(i)
    print('This will be the card you begin this bingo game with!')
    flag = True
    while flag == True:
        player_response = str(input('Is it time to choose a new item?: '))
        if player_response == 'yes' or player_response == 'Y':
            card_display = bingoCard[0][0:], bingoCard[1][0:], bingoCard[2][0:]
            for i in card_display:
                print(i)
                random_choice_all_data = random.sample(website_list, 1)
                for y in range(0,3):
                    for j in range(0,3):
                        if bingoCard[y][j] == random_choice_all_data[0]:
                            bingoCard[y][j] = 'SEEN'


                if bingoCard[y][0] == bingoCard[y][1]== bingoCard[i][2] == 'SEEN':
                    print('Since you have gotten three across, you have won this bingo game!')
                    flag = False
                elif bingoCard[0][0] == bingoCard[0][2] == bingoCard[2][0] == bingoCard[2][2] == 'SEEN':
                    print('Since you got all four of the corners, you have won this bingo game!')
                    flag = False


def main():
    '''
    The purpose of this function is to serve as a call to all the other functions in this program that perform their respective tasks as well as a record of the important information
    the functions will need to perform tasks efficiently.
    there are no specific parameters for this main() function however there are parameters mentioned for each of the respective other functions called below.
    :return: there is 'no official return word' in this function. However there is the main function called at the end.
    '''
    url = 'https://research.cs.queensu.ca/home/cords2/zoombingo.txt'  # making the url a string
    response = urllib.request.urlopen(url)
    data = response.readline().decode('utf-8')
    website_list = website_reading(url)
    bingoCard = bingo_card_creation(website_list)
    play(bingoCard, website_list)


main()
