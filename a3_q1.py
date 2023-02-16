"""
This program will allow the user to play a dice game by simulating two dice rolls with 4 rules that lead to different commands in the game
Date: Sept/Oct 2022
"""
#assigns initial values to variables to be used. Import random allows dice to randomly generate numbers when rolled.
import random
total_points = 0
dice1 = 0
dice2 = 0
roll_count = 1
rolls = 0
response_user = 'y' or 'Y'
stopPlay = 'False'
#this prints the first line of output "Welcome to the very fun dice game"
print('Welcome to the very fun dice game')
#this line will ask the user if they would like to play the game or not: if they press 'Y' or 'y' the game continues.
response_user = input('Would you like to play (type Y or y)?: ')
#this line represents the format created for the code including the 4 rules. There is one big while loop which contains all the four condition rules written as if and elif statements.
while response_user == 'y' or response_user == 'Y':
#the two line includes the two dice numbers generator for die1 and die2
    die1 = input(random.randint(1, 6))
    die2 = input(random.randint(1, 6))
#this line represents the condition rule1 where both numbers rolled are the same number(doubles) ex: you roll two 2's. In that case: the program will reroll die 2 up until there are two different values of die1 and die2
    #then calculating the total points from the roll/s leading up to the roll with different numbers (this does not include the very first roll that got us to this point).
    # it prints the numbers rolled and the total score when applicable
    if die1 == die2:
        while die1 == die2:
            die2 = input(random.randint(1, 6))
            roll_count += 1
            print('Roll Number', roll_count, ': ', die1, " ", die2, sep='')
        total_points += (die1 + die2 + roll_count)
        print('The numbers rolled are' + str(die1) + str(die2) + '')
        print("The total score is: ", total_points)
#the lines below represents the condition rule #2 scenario where the resultant points from the two dice equal an even value. If even: the dice will roll 4 times then the sum will be added up and stated. the numbers rolled are also stated.
    elif (die1 + die2) % 2 == 0:
        print('The sum of ', die1, 'and', die2, 'is an even number so roll the dice 4 times.')
        for rolls in range(1, 5):
            roll_count += 1
            die1 = input(random.randint(1, 6))
            die2 = input(random.randint(1, 6))
            total_points += (die1 + die2)
            print('Roll Number: ', roll_count, ': ', die1, " ", die2, sep='')
            print('The numbers rolled are' + str(die1) + str(die2) + '')
            print("The total score is: ", total_points)
#the lines below represents the condition rule #3 scenario where either die1 or die2 lands a 3. If this happens play stops.
    elif die1 == 3 or die2 == 3:
        print('You have rolled a 3')
        if stopPlay == 'True':
            total_points += 3
            print('You rolled ' + 'str(die1)' + 'and' + '+str(die2)+ '')
            print('You have', total_points, 'points')
#the lines below represents the condition rule #4 scenario where a magic 7 total points value is landed. If this happens: Program doesn't add 7 points to total.
#instead will add 10 points to points total then roll 10 more times. Each time addinf sum of dice to points total.
    elif die1 + die2 == 7:
        print('The sum of', die1, 'and', die2, 'is a magic number and you have gained 10 points! ')
        for rolls in range(10):
            die1 = input(random.randint(1, 6))
            die2 = input(random.randint(1, 6))
            print('Roll Number', roll_count, ':', die1, '', die2, sep='')
            total_points += die1 + die2 + 10
            print('You have', total_points, 'points')
            print("The total score is: ", total_points, "points")
#thes lines below add the dice together and state their values and their total points if none of the 4 condition rule scenarios applicable.
    else:
        total_points += die1 + die2
        print('You rolled' + str(die1) + 'and' + str(die2))
    if stopPlay == 'True':
        response_user = 'N'
    else:
        response_user = input('Would you like to continue playing?')
        print("The total score is: ", str(total_points) + '')
