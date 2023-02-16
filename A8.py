"""
This program will read a list of words into our program and run some specified statistics on them.
Date: November 2022
"""








import urllib.request
url = "https://research.cs.queensu.ca/home/cords2/words.txt"
response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")
print(data)

def readWords(url):
    """
This function function takes one parameter, the URL from which to read the text, and it also will return a list of strings where each element is a word found on the website
parameter - url
return - data, reads information into single string. URL passed as string.
    """
        try: #try and except used if something goes when opening / handling URL
            response = urllib.request.urlopen(url)
            data = response.read().decode("utf-8")
            important_words = data.split()
        except:
            print('It is unclear as to what occurred and can not connect to URL currently speaking')
            return important_words




def wordCount(wordList):
    """
This function takes 1 parameter, list of strings (ie. the list of words that were read in from the website, but the function can take any list of words
parameter - wordList
return - dictionary of key/value pairs where the key is an integer representing the number of letters in a word and the value is an integer indicating the number of words in the list of strings that are of each length
    """
   words = {}
   for string_x in wordList:
       length_word = len(string_x)
       if length_word in words:
           words[length_word] = words[length_word] + 1
       else:
           words[length_word] = 1
           return words




def totalWords(words, n, m):
    """
This function takes the dictionary of length/frequency pairs along with two integer values, n and m and returns the total number of words of lengths n to m (inclusive).
parameter - words, n and m values
return - either value of n + m (total number of words addition) or return 0
    """
    if n < m:
        t = 0
        for i in range(n, m+1):
            total = total + words.get(i, 0)
        return total
    else:
        print('Unfortunately n was greater than m')
        return 0



def maxWordLength(words):
    """
This function  take as parameters the dictionary or length/frequency pairs and will each return an integer
parameter - words (dictionary)
return - max(list_key)
    """
    list_key = []
    for key in words:
        list_key.append(key)
    return max(list_key)


def maxFrequency(words):
    """
This function  take as parameters the dictionary or length/frequency pairs and will each return an integer
parameter - words (dictionary)
return - max_possible_frequency
    """
    for key in words:
        for val in words.values():
            if words[key] > val:
                max_possible_frequency = words[key]
    return max_possible_frequency

def writeToFile(words):
    """
This function takes a dictionary of length/frequency pairs as a parameter and writes it to a file in this format (all data should be included) and opens file statWords.txt
parameter - words (dictionary)
return - either 0 or writes file into proper format
    """
    if len(words) <= 0:
        return
        file = open('statWords.txt', 'w')
        for w in words:
            f = file.write(('In this scenario there will be ' + 'str(words.get(w))' + 'words belonging to the length' + 'str(w) +''\n'))
        file.close()
    else:
        return 0

def main():
    """
call to main function calls all other functions and does testing
parameter - none directly
return - all functions and actions in program
    url = "https://research.cs.queensu.ca/home/cords2/words.txt"
    print(readWords(url))
    words = {}
    print('dictionary for word count: ',)
    n = 5
    m = 13
    print('The total word function when n =5 and m = 13 will be:', totalWords(words, n, m))
    n = 5
    m = 14
    print('the total word function when n = 5 and m = 14 will be:', totalWords(words, n, m))
    n = 19
    m = 8
    print('total word function when n = 19 abd m = 8 will be:', totalWords(words, n, m))
    print('the max length possible is', maxWordLength(words))
    print('the max frequency possible is', maxFrequency(words))
    writeToFile(words)


main()
