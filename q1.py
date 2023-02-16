"""
This program calculates the amount of cupcakes you must bake considering your study group friends and their pets
Date: Sept 2022
"""
#the two lines below give the the cupcakes we must bake per person and the cupcakes per pet respectively 
cupcakesper_person = 2
cupcakesper_pet = 1
#the line below states the number of people coming to the study group (including yourself)
people = int(input("how many people are coming to your study group: "))
#this line shows the combined total of pets belonging to the study group
pets = int(input("how many of these people have pets?: "))
#this line says the number of cupcakes you must bake for yourself
cupcakesforlater = 4
#this line does the calculations needed to determine how many cupcakes must be baked
total_cupcakes = (int(cupcakesper_person) * int(people) + int(pets) + int(cupcakesforlater))
#the last line states the amount of cupcakes that you need to bake
needed_cupcakes = input("You should bake " + str(total_cupcakes) + " cupcakes")