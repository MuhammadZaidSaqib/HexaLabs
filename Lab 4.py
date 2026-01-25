#Name : Muhammad Zaid Saqib
#Reg: B24F1722CYS084
#3rd  Semester
# Introduction to AI
#Date : 23 September 2025
#lab 4



#Lab practice

#Topic List

# Practice Task 1
#Make list

'''
list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print("The sum of all entered numbers is:", sum(list)) '''

#Practice Task 2
#Indexing
'''
print(list(0))
print(list(-1))
print(list(3))
'''

#Practice Task 3
#update
'''
list[2]=79
print(list)'''


#Practice Task 4
#use of append
'''
list.append(95)
print(list)'''


#Practice Task 5
#using insert
'''
list.insert(7,69)
print(list)'''

#Practice Task 6
#slicing
'''
print(list[:9])
print(list[-16:-1])
'''
# Practice Task 7
# sort

'''list=[365,364,397,7994,745]
list.sort()
print(list)
'''

# Practice Task 8
#reverse sort
'''
list.sort(reverse=True)
print(list) '''

#Practice Task 9
#remove first occurrence

'''list=[2,1,3,1,4,5,6,3]
list.remove(4)
print(list)'''

#Practice Task 10
#remove single element
'''list=[2,1,3,1,4,5,6,3]
list.pop(5)
print(list)'''

#lab task
#list


#Q1Create a list of 5 student names and print them one by one using a loop.
'''
students=['Ali','Umar','Hassan','Hussain','Ayesha']
for student in students:
    print(student)'''

#Q2: Take 5 numbers as input from the user, store them in a list, then print the list in reverse order.
'''
numbers=[]
for i in range(5):
    num=int(input("Enter a number: "))
    numbers.append(num)
numbers.reverse()
print("Numbers in reverse order:",numbers)
'''

# Q3:: Write a program that finds the maximum, minimum, and average of this list:
# e.g marks = [78, 56, 89, 92, 65, 73]

'''
marks = [78, 56, 89, 92, 65, 73]
max_marks = max(marks)
min_marks = min(marks)
avg_marks = sum(marks) / len(marks)
print("Maximum marks:", max_marks)
print("Minimum marks:", min_marks)
print("Average marks:", avg_marks)
'''

#Q4: Write a program to count how many times a number 5 appears in a list.
'''
numbers = [1, 5, 3, 5, 7, 9, 5, 2, 4,5,6,9,7,3,6,4,5,5]
count_5 = numbers.count(5)
print("The number 5 appears", count_5, "times in the list.")
'''


# Topic Tuple

#Practice Task 1
#Create Tuple
'''
Tup=(2,1,3,1,4,5,6,3)
print(Tup)'''


#Practice Task 2
#indexing in tuple
'''
tup=('umar','ali','hassan','King Jawad Khokhar')
print(tup[1:])
print(tup[0])
print(tup[-1])
'''

#Practice Task 3
#count  tuple
'''
tup=('umar','ali','hassan','King Jawad Khokhar','ali','ali')
print(tup.count('ali'))
print(tup.index('hassan'))
print(len(tup))'''

#Practice Task 4
#slicing
'''
print(tup[1:4])
print(tup[-4:-1])
'''

#Practice Task 5
#convert list to tuple
'''
list=[2,1,3,1,4,5,6,3]
tup=tuple(list)
print(tup)'''

#Practice Task 6
#convert tuple to list
'''
tup=('umar','ali','hassan','King Jawad Khokhar','ali','ali')
list=list(tup)
print(list)'''

#Lab Task
#Tuple

#Q1: Convert a tuple of fruits into a list, replace one fruit, and convert it back
'''
fruits_tuple = ('apple', 'banana', 'cherry', 'date')
fruits_list = list(fruits_tuple)
fruits_list[1] = 'blueberry'
furits_list[2]='mango'
fruits_tuple = tuple(fruits_list)
print("Updated tuple:", fruits_tuple)
'''

#Q2: Given a tuple (2, 4, 6, 8, 10, 12), calculate and print the sum of all numbers.
'''
tup=(2, 4, 6, 8, 10, 12)
print("The sum of all numbers in the tuple is:", sum(tup))
'''

#Q3: Create a tuple containing the days of the week. Print only weekends.
'''
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
weekends = days_of_week[5:]
print("Weekends are:", weekends)
'''

#lab Practice
#Topic Dictionary

#Practice Task 1
#Create Dictionary
'''
dict={'name':'Zaid ','age':22,'city':'In her eyes '}

print(dict)'''

#Practice Task 2
#Updating
'''
dict['age'] = ' dead long ago '
'''

#Practice Task 3
# Adding
'''
dict["dream"]=" fake death "
print(dict)
'''
#Practice Task 4
#deleting
'''
del dict['age']
print(dict)
'''

#Lab Tasks


#Q1 Create a dictionary of 3 students with their names as keys and marks as values. Print each student with their marks.
'''
student={'Ali':85,'Umar':90,'Hassan':78}
for name,marks in student.items():
    print(name,":",marks)
'''

#Q2 Add a new student to the dictionary and update one student’s marks.
'''
for i in range(2):
    print()
print("After adding new student and updating marks:")
for i in range(2):
    print()

student['Ayesha']=88
student['Minha ']=95
for name,marks in student.items():
    print(name,":",marks)

'''
#Q3 Write a program that counts the frequency of each word in a sentence
'''
sentence = (input("Enter a sentence: "))
words = sentence.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print("Word frequency:", word_count)
'''
#Conculsion

'''
I worked with Pythons fundamental data structures in this lab, including **lists, tuples, and dictionaries, 
and learned how to construct, modify, and work with them in various ways.  Along with tasks like publishing student names,'
storing user input, determining maximum/minimum/average marks, and counting occurrences of a number,'
I worked with lists to practice indexing, slicing, inserting, appending, sorting, reversing, and removing components.'
I gained knowledge about creating and accessing elements, counting occurrences, slicing, converting between lists and tuples, 
and resolving issues like printing weekends from the days of the week, altering tuples, and adding integers.  I worked on building,
updating, adding, and removing key-value pairs using dictionaries. I also used them for tasks like counting word frequencies in sentences
and storing and updating student grades.'''



















