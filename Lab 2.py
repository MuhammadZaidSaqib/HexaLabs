# Muhammad Zaid Saqib
# B24F1722CYS084
# 3rd Semester
# Introduction to AI
# Lab 2

# Lab Practise

# Q1.Write a program to calculate the age of a person after 5 years.
'''age = input("Enter the age ")
print("Your age is ",int(age) +5)'''

# Q2.Write a program to calculate the height of a person in meters.

'''height = float(input("Enter the height in meters "))
print("Your height is ",height," meters") '''

# Q3.Print 3 Numbers in a single line.

'''x,y = input("Enter two numbers ").split()
print(" Value of x is ",x," and value of y is ",y) '''

# Q4.Print 4 Numbers in a single line.

'''x,y,z,w = input("Enter Four numbers ").split()
print(" Value of x is ",x," and value of y is ",y," and value of z is ",z," and value of w is ",w) '''

# Q5.Print 2 Strings in a single line.

''' string1 = "hello"
string2 = "world"
print(string1)
print(string2)  '''

# Q6.Concatenate 2 strings and print the result.

'''string="Hello"
string=string+" World"
print(string) '''

# String Concatenation

''' first = "Cyber"
second = "Security"
result = first  + second
print(result) '''

# string repetition

'''string = " hacked "
result = string * 3
print(result) '''


# string indexing

'''text = "Python is an easy language &&&$*&%"
print(text[0])  #First character
print(text[10]) #fourth character
print(text[-1]) #last character '''

#string slicing

'''text = "ComputerScience  Department"
print(text[0:5])  #character from index 0 to 5
print(text[2:])    #character index from 2 to end
print(text[:6])    #character index from 6
print(text[-7:])   #last seven character '''

#String Methods (Useful Functions)

'''text = "  Machine Learning  "

print(text.lower())    # all lowercase
print(text.upper())    # all uppercase
print(text.strip())    # remove spaces from start and end
print(text.replace("Learning", "Intelligence"))  # replace word
print(len(text))       # length of string '''

# lab Task

# 1: Write a Python program that Asks the user to enter their name and age using input().
#Prints a sentence using an f-string.


''' name = (input("Enter your name "))
age = int(input("Enter your age "))

print(f"My name is {name} and I am {age} years old") '''


#2: Write a program that:Takes a string input from the user.Prints the following:
#First character of the string.
#Last character of the string.
#Length of the string.
#The string in uppercase

text = input(" Enter your message ")
print(f" The First letter is:",text[0])
print(f" The last letter is :{text[-1]}")
print(f" The length of the message is : {len(text)}")
print (f" String in  uppercase :",text.upper())
print (f" String in  lowercase :",text.lower())


