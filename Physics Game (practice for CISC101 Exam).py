#Weight in the universe. Calculates weight of the user on the earth and
#then calculate what the player's weight would be on
#Earth, Moon and Mars

def weight(weight_in_n):
    '''
    the purpose of this function is to calculate the player's weight on the earth
    :param weight_in_n: weight_in_n represents the weight in newtons
    :return: this function returns the weight in newtons on the earth
    '''
    mass = float(input('Enter a value of mass: '))
    gravity = 9.8
    weight_in_n = mass * gravity
    return weight_in_n
    print('based on the mass value entered, your weight on the earth is', weight_in_n)
    return weight_in_n

def moon_weight(weight_on_earth):
    '''
    the purpose of this function is to calculate the player's weight on the moon
    :param weight_on_earth: weight_on_earth represents the weight in earth
    :return: this function returns the weight on the moon
    '''
    moon_conversion = 0.165   #percentage of your weight on earth when on moon
    your_weight_on_moon = weight_on_earth * moon_conversion
    return your_weight_on_moon
    print('based on the mass value entered, your weight on the moon is', your_weight_on_moon)
    return your_weight_on_moon


def mars_weight(weight_on_earth):
    '''
    the purpose of this function is to calculate the player's weight on mars
    :param weight_on_earth: weight_on_earth represents the weight on earth
    :return: this function returns the weight on mars
    '''
    mars_conversion = 0.38
    your_weight_on_mars = weight_on_earth * mars_conversion
    return your_weight_on_mars
    print('based on the mass value entered, your weight on mars is', your_weight_on_mars)
    return your_weight_on_mars

def main(weight_in_n):
    '''
    serves as the main place for calling functions and the user interface.
    :return: no particular return. The function will print and return as required.
    '''
    user_input = input('Would you like to play this physics(forces) inspired game (Y or N): ')
    if user_input == 'Y':
        weight_on_earth = weight(weight_in_n)
        menu_of_options = int(input(
            'the following are the options for tracking your weight on different terrains(Enter a value corresponding to a location in the universe):\n'
            '1. Weight on the Earth\n'
            '2. Weight on the Moon\n'
            '3. Weight on Mars\n'))
        while 0 < menu_of_options < 4:
            if menu_of_options == 1:
                weight(weight_in_n)
            elif menu_of_options == 2:
                moon_weight(weight_on_earth)
            elif menu_of_options == 3:
                mars_weight(weight_on_earth)
            else:
                print('invalid entry')
    else:
        print('It seems you are no longer interested in playing this game\n hopefully you will join us next time\n')


main('weight_in_n')
