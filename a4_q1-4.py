"""
This program uses 4 functions to answer the 4 questions given. 1) printing a poem where the name can change every time 2) takes 2 integers as parameters (n and m), returns
product of squares of each of values from n to m. 3)converts canadian dollar to chinese yuan 4)Menu that allows user to pick which of the 3 functions to run.
Date: 8 Oct 2022
"""
def poem():
   """
This function prints the poem but customizes it so that there will be a different person's name each time.
Parameters: print("Loops were crazy,") , print("What are functions about?"), print("you can do this"), print("Just stick it out!")- 4 poem lines name() - function inside the poem function.
Return Value - the poems lines with the name inputted by the user
   """
#the print statements in the poem function (stated below) represent the poem's lines and also include the name function which has the name entered by the user (Q1).
    print("Loops were crazy,")
    print("What are functions about? ")
    name(), print("you can do this")
    print("Just stick it out! ")


def name():
   """
   the name function below is the function that is inside the poem function (inner function/nested function) which through use of input allows the name mentioned in poem to be customizable.
   Parameters: input('name: ') - allows user to input a name for poem
   Return Value - the name inserted by user
   """
#line below lets user input name. The lines above are part of Q1.
    input('name: ')



# below are the lines that help to perform the calculations for Q2: product of square of n and m.
def numbers_product_square(n, m):
   """
   This function takes the product of square of all values between n and m.
   Parameters: n and m - values the user inputs. the if statement places the restrictions(error check) defined in question: if n>m or more than 4 digits involved return 0. For loop loops from n to m. As the loop does the multiplication it increases by 1.
   Return value - function returns final result of the product of square from n-m inclusive multiplication.
   """
# the lines below upto return result will calculate the product of square and then return the value.
    if n > m or abs(n - m) > 4:
        return 0
    result = 1
    for i in range(n, m + 1):
        result *= i * i

    return result


# below are the lines that perform the conversion of a Canadian dollar value to Chinese Yuan Currency for Q3.
def dollars_conversion_yuan(d):
   """
   This function takes the canadian dollar amount inputted by the user and multiplies it by 5.19 to attain the Chinese Yuan equivalent value.
   Parameters: d - representing dollars(Canadian) , 5.19 - the value we must multiply with in order to get our final converted value in Chinese Yuan.
   Return Value - function returns converted numerical amount in Chinese Yuan
   """
#the lines below perform and return the calculation needed to answer Question 3. 
    d * 5.19
    return d * 5.19


#written below are the lines of code allowing the user to choose which function (numbered 1-3) they would like to run and see in action.
def menu():
   """
   This function takes the order choice inputted (1-3) by the user to allow a function to run and solve one of the questions. The choices are numbered after the aforementioned questions numbering.
   Parameters: if statement for when order is 1 means poem function is run. Order = 2 means product of square function is run. Order = 3 means CAD to Chinese Yen function is run.
   Return Value - this function will bring us to the function corresponding to the number entered by the user. If the value entered is not 1-3: no additional function is run.
   """
#the lines below state that if order =1 poem function returned. It will print user friendly statements that guide the user if they run function 2: telling them they chose this function and asking for values of n and m so calculation is made.
#If user chooses 3: program asks user to enter amount of canadian dollars they wish to convert, stating the final converted value. If user chooses 4 the program prints "program ended"
#If user chooses anything else program will print invalid input and thanks for using. menu() is placed at end so that user is asked initial choice question. 
    order = int(input("Enter a choice from 1-3: "))
    if order == 1:
        poem()
    elif order == 2:
        print('You have selected the product of square function')
        n = int(input('Enter the first integer: '))
        m = int(input('Enter the second integer: '))
        print(numbers_product_square(n, m))
    elif order == 3:
        d = int(input('Enter the amount of Canadian dollars you wish to convert: '))
        dollars_conversion_yuan(d)
        print('The final converted value is: ' + str(dollars_conversion_yuan(d)) + 'yuan')
    elif order == 4:
        print('program ended')
    else:
        print("invalid input")
        print("Thanks for using")


menu()
