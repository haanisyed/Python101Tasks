"""
The purpose of this program is to serve as an application that uses this data (from Downtown Toronto bike stations) to keep track of the information (stationId, name, capacity, bikes available, docks available) process bike rentals and returns.
Date: Nov 2022
"""





def initializeBikeInfo():
    """
        This function defines the dictionary that will hold all the information.
        The dictionary is of the format:
            stationID (key): value is a dictionary
            So, for example an entry for station ID = 70 might look like:
                70: {"location": "Jarvis", "cap": 50, "numBikes": 4, "docks":2}
        A dictionary containing all the stations' info is returned.
        Parameters:  None
        Return:  A dictionary
    """

    ###code for main big dictionary (d_toronto_bikes: main data structure in program) for downtown Toronto bikes is mentioned below to form the dictionary holding the
    ###rental information contained in the table in the assignment instructions (location, capacity, number of bikes, docks availability).
    ###This dictionary has 8 keys (one for each station ID)
    ###the keys exactly as shown in the example are used so that the test code
    ###will work.
    ###this main data structure (big dictionary: d_toronto_bikes) is returned.

    d_toronto_bikes = {
        8010: {'location': 'York', 'cap': 31, 'numBikes': 20, 'docks': 11},  #this mentions the data for the stationId of 8010 (key) while the rental information dictionary(value).
        8011: {'location': 'Esplanade', 'cap': 15, 'numBikes': 5, 'docks': 10}, #this mentions the data for the stationId of 8011 (key) while the rental information dictionary(value).
        8012: {'location': 'George', 'cap': 19, 'numBikes': 1, 'docks': 18}, #this mentions the data for the stationId of 8012 (key) while the rental information dictionary(value).
        8013: {'location': 'Madison', 'cap': 15, 'numBikes': 2, 'docks': 13}, #this line mentions the data for the stationId of 8013 (key) while the rental information dictionary(value).
        8014: {'location': 'Elm', 'cap': 11, 'numBikes': 0, 'docks': 11}, #the line mentions the data for the stationId of 8011 (key) while the rental information dictionary(value).
        8015: {'location': 'University', 'cap': 19, 'numBikes': 1, 'docks': 18}, #this line mentions the data for the stationId of 8015(key) while the rental information dictionary(value).
        8016: {'location': 'Bay', 'cap': 11, 'numBikes': 11, 'docks': 0}, #this line mentions the data for the stationId of 8016(key) while the rental information dictionary(value).
        8017: {'location': 'College', 'cap': 11, 'numBikes': 1, 'docks': 10} #this line mentions the data for the stationId of 8017(key) while the rental information dictionary(value).
    }
    return d_toronto_bikes #the main data structure dictionary for downtown Toronto bikes (d_toronto_bikes) is returned.


# dictionary structure = {stationID: {location, capacity, bikes available, docks available} }.
# {location, capacity, bikes available, docks available} this dictionary(rental information) within the main dictionary 'd_toronto_bikes' is referred to as 'bikeInfo'.


def changeInfo(bikeInfo, id, cap, numBikes, docks):
    """
           This function changes the capacity, number of bikes available and the
           number of empty docks for the given (id) station.
           Parameters:  bikeInfo - a dictionary
                        id - integer indicating the location id
                        cap - integer - number of bikes that the station accommodates
                        numBikes - how many bikes are currently available for rent
                        docks - how many docs are currently free
           Returns:  Nothing returned, but bikeInfo is updated.
    """
    if 'cap' in bikeInfo[id] and 'numBikes' in bikeInfo[id] and 'docks' in bikeInfo[id]: #this if statement ensures that the next 3 lines of code will be able to make their specific desired changes/alterations.
        bikeInfo[id]['cap'] = cap #this line changes the capacity value(from rental information dictionary) for the given id station
        bikeInfo[id]['numBikes'] = numBikes #this line changes the number of bikes value (numBikes) (from the rental information dictionary) for the given dictionary.
        bikeInfo[id]['docks'] = docks #this line changes the number of docks value(docks)(from the rental information dictionary) for the given dictionary.


def bikeRental(bikeInfo, stationId):
    """
            Checks to ensure that stationID is a valid station in bikeInfo.
            If so, checks to see if there are bikes available at this station.
            If so, decrements the number of bikes available for rent at this station and increases
            the number of available docks.
            Parameters: bikeInfo - a dictionary
                        stationID -- integer representing the ID of the station from which to rent
            Returns:  True (bike was rented successfully), False (something went wrong)
                      bikeInfo may be updated.
    """
    ###code added here is to process a bike rental.
    ###The def bikeRental function does not print anything nor does it ask the user for any input.
    ###def bikeRental will just return True or False depending on the situation.
    if stationId in bikeInfo:
        bikes_available = bikeInfo[stationId]['numBikes']
        if bikes_available > 0:
            bikeInfo[stationId]['docks'] = bikeInfo[stationId]['docks'] + 1
            bikeInfo[stationId]['numBikes'] = bikeInfo[stationId]['numBikes'] - 1
            return True #returns True.
        else: #if bikes available is not greater than zero. Then the program will return "False".
            return False #returns False.
    else: #if the particular stationId is not found in the bikeInfo. The program will return "False".
        return False #returns False.


def returnBike(bikeInfo, stationId):
    """
            Indicates whether or not a bike can be returned to the given station ID.
            Need to check if stationID is valid.  If not, return False (bike can't be returned here).
            A bike can be returned if there are available docks, otherwise it cannot be returned
            to that location.
            Parameters:  bikeInfo - a dictionary
                         stationID - an integer
            Returns: True if a bike can be returned, False otherwise
    """
    ###The code added here is used to implement the functionality described in comment. It will inform whether a bike can or can not be returned to the particular given station Id.
    if stationId in bikeInfo: #this line represents that if a bike can be returned (if stationId is in bikeInfo), True will be the return.
        return True #returns True.
    if bikeInfo[stationId]['docks'] > 0: #this line indicates that if a bike can be returned (the value of docks is greater than zero). The program will return "True".
        return True #returns True.
    else: #this line implies that if a bike can not be returned. The program will return "False".
        return False #returns False.


def getInfo(bikeInfo, stationId):
    """
            This function looks up the information found at stationID in bikeInfo
            and returns the location, capacity, bikes available and docks in a list.
            If stationID does not exist in bikeInfo, return an empty list.
            Parameters:  bikeInfo - a dictionary of the format {stationID: {values}}
                         stationId - integer
            Return: a list [location, capacity, bikesAvailable, docks] or []
    """
    empty_list = [] #when a stationId that has not been covered explicitly in the main data structure (d_toronto_bikes dictionary) is brought up. the "empty_list" will be returned.
    if stationId in bikeInfo: #this line represents the fact that if the stationId is in bikeInfo(data structure) only then we will be able to return its exact location, capacity, number of bikes, and docks availability.
        return [bikeInfo[stationId]['location'], bikeInfo[stationId]['cap'], bikeInfo[stationId]['numBikes'], bikeInfo[stationId]['docks']] #this line represents the exact location, cap, numBikes, and docks to be returned for the specific station.
    else: #if the stationId mentioned is not found in the main data structure (d_toronto_bikes dictionary) then an empty list will be returned for that specific studentId because it was outside of the range of values mentioned in the main data structure.
        return empty_list #this line will return an empty list [].


def docksAvailable(bikeInfo):
    """
             This function returns the total number of docks available across all
             locations.
             Parameters:  bikeInfo - a dictionary of the format {stationID: {values}}
             Return: integer
    """
    docks_total = 0 #sets the total docks initially to zero
    for stationId in bikeInfo: #this line represents the fact that we are specifically looking for station Id that are within bikeInfo.
        for y in range(8010, 8017): #this line represents the acceptable range for station Id which this program deems acceptable and for which further important values such as rental information have been given in the main data structure (d_toronto_bikes).
            docks_total = docks_total + bikeInfo[y]['docks'] #this line calculates the total docks available across all locations in Downtown Toronto. "y" representing the stationId.
    return docks_total #this line will return the exact number of docks available across all locations in downtown Toronto.


def testCode():
    """
This function is to be included into the program as it contains print statements that will return the required and desired output to be able to complete this program.
Parameters - not directly applicable. Instead there are many print statements and code written below that connect to the program's findings above and state them as sentences.
Return: no direct use of the word "return" in this testing code function. However there are many print statements that reveal the many findings from the program with regards to Downtown Toronto bikes to the user.
    """
    # Test initialize function
    info = initializeBikeInfo()
    print(info)
    print()

    # Test change info
    changeInfo(info, 8012, 15, 7, 8)
    print("After changing information for 8012, new info is:")
    print(info)

    # Test bike rental when bikes not available
    print("Number of bikes at 8014 before renting is", info[8014]["numBikes"])
    bikeRental(info, 8014)
    print("Number of bikes at 8014 after renting is", info[8014]["numBikes"])

    # Test bike rental when bikes  available
    print("Number of bikes at 8011 before renting is", info[8011]["numBikes"])
    bikeRental(info, 8011)
    print("Number of bikes at 8011 after renting is", info[8011]["numBikes"])
    print("Number of docks at 8011 after renting is", info[8011]["docks"])

    # Test information retrieval for a specific location that doesn't exist
    statInfo = getInfo(info, 1010)
    if len(statInfo) == 0:
        print("Station does not exist")
    else:
        print("Info for station 1010 is ", statInfo)

    # Test information retrieval for a specific location that exists
    statInfo = getInfo(info, 8010)
    if len(statInfo) == 0:
        print("Station does not exist")
    else:
        print("Info for station 8010 is ", statInfo)

    # Test to find total number of docks available
    print("Total number of docks available: ", docksAvailable(info))

    # Test bike return - run through all cases
    for key in info:
        if returnBike(info, key):
            print("Returned bike successfully to ", key)
        else:
            print("Could not return bike to", key)


testCode() #call to testCode() function
