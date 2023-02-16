"""
This program The program stores a list of students and 4 assignment marks for each student.  Each student is represented as a tuple with two values, the student's name and a list of marks (studentName, [list of marks]). Includes functions that perform actions on this data set such as finding the average for a particular student, adding a new student, finding the class average on an assignment etc. 
Date: October 2022
"""





def printMark(list_students, student_name):
"""
Function 1 of Assignment 5 [def printMark()] - this function prints lists of students and their marks.
Parameters - takes 2 parameters: entire list of students + their marks + name of student. Need to add 2 parameters to function decalaration
Return values - prints students' names and their marks. If student name entered doesn't exist: there will be no explicit returned value, and print statement issued instead.
"""




    printing_mark = False
    for item in list_students:
        for studs in item:
            if student_name in studs:
                student_index = studs.index(student_name)
                student_marks = item[student_index + 1]
                printing_mark = True

    if printing_mark is True:
        print("The marks for " + student_name + " are: ")
        count = 0
        for marks in student_marks:
            count += 1
            print("A" + str(count) + ": " + str(marks))

    else:
        print('No student by that name. There will be no explicit returned value for this function')
    return []

def averageAssignment(list_students, number_assignment):
"""
Function 2 of the Assignment 5 [def averageAssignment(list_students, number_assignment)] - this function calculates average for given assignment and returns average.
Parameters - takes 2 parameters: entire list of students and integer indicating which assignment (0,1,2,3) you would like to find average for.
Return values - returns the average for the given assignment. If the assignment number is not: 0,1,2,3 then the function will return -999
"""






    if 4 < number_assignment < 0:
        return -999
    else:
        average = 0
        for i in range(len(list_students)):
            average += list_students[i][1][number_assignment]
            average /= len(list_students)
        return average



def averageMark(list_students, student_name):
"""
Function 3 of the Assignment 5 [def averageMark(list_students, student_name)] - this function calculate and returns average overall marks for students.
Parameters - takes 2 parameters: entire list of students and their respective data, and uses that data to calculate average for each student of their 4 marks in the data set.
Return values - returns the exact average of the dataset for a student. If the student name chosen does not exist in the dataset, 0 is returned.
"""





    for i in list_students:
        if i[0] == student_name:
            average = 0
            for j in i[1]:
                average += j
            average /= len(i[1])
            return average

def highestAverageMark(list_students):
"""
Function 4 of the Assignment 5 [def highestAverageMark(list_students)] - this function calculates average for each student and returns the student/s names who have the highest Average Mark.
Parameters - takes parameter: list of all students and their data.
Return Values - returns the name/s of the student/s who have the highest average mark. If list is empty, it returns empty list.
"""






    average_highest = 0
    averages_student = []
    names_student = []
    students_best = []

    for student in list_students:
        name = student[0]
        names_student.append(name)
        average = averageMark(list_students, name)
        averages_student.append(average)
        if average > average_highest:
            average_highest = average

    for index in range(len(averages_student)):
        if averages_student[index] == average_highest:
            students_best.append(names_student[index])
        return students_best

def increaseMarks(list_students):
"""
Function 5 of the Assignment 5 [def increaseMarks(list_students)] - this function calculates all marks of all students after 1 mark is added to each
Parameters - given a list of students (1 parameter) function will calculate the marks after 1 mark is added to all in the dataset
return - function should not return anything
"""




    for student in list_students:
        for i in range(len(student[1])):
            student[1][i] = student[1][i] + 1


def addNewStudent(student_name):
"""
Function 6 of the Assignment 5 [def addNewStudent (student_name)] - this function takes list of students and marks to allow a new student to be added along with their 4 marks
Paramerers - student names and marks (one parameter - student_name)
return - This function has no explicit return. The function will prompt the user for name of student and their 4 marks and will add students name to list only if it is unique when compared to the other names in the dataset. If the new name is the same as one of the names already present, user will be repeatedly prompted to enter a new name.
"""


    if student_name == "Jane" or student_name == "Xinrong" or student_name == "Sima":
        print('This name already exists. Please enter a new name')
    else:
        print("The new student's name and marks are:", student_name)

def main():
"""
function 7 of the Assignment 5 [def main()] - this function contains the dataset (tuple with the three students (Jane, Xinrong, Sima) names and marks) which is used by all of the remainder functions to be able to complete their operations and jobs.
Parameters - none inside the brackets of def main(). There are references to parts of calculations and user friendly print statements inside the function with explanations.
return - This function starts the entire program once the user calls it main(). It contains calculations and important code for each function. 
"""










    students = [("Jane", [80, 74, 93, 60]), ("Xinrong", [72, 89, 55, 75]), ("Sima", [93, 80, 74, 60])]
    print("Here is the data set", students)
    print("This program doesn't do anything yet. Complete the program as per the comments")

    printMark(students, "Xinrong")
    printMark(students, "Sima")
    printMark(students, "Haani")

    averageAssignment(students, 1)
    assignment_average_mark = averageAssignment(students, 1)
    print(" The average mark for assignment 1 is:", assignment_average_mark)


    print("The average mark for Jane is:" ,averageMark(students, "Jane"))
    print("The average mark for Haani is:" ,averageMark(students, "Haani"))

    names_highest = highestAverageMark(students)
    names = ""
    count = 0
    for i in names_highest:
        count += 1
        if count == len(names_highest):
            names += "and " + i
        else:
            names += i + ", "
    print(" The students with the highest average marks are", names)

    addNewStudent(students)
    student_name = input('name of student [4 marks with commas in brackets]:')
    print(students)

    increaseMarks(students)
    print('Marks for students after adding 1 mark to each mark are now:', students)


main()
