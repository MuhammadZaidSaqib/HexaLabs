# Muhammad Zaid Saqib
# B24F1722CYS084
# 3rd Semester
# Introduction to AI
# Lab 3

# Lab Practise

# if else code


# if else

'''age=16
if age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")'''

# if without else

'''temperature =int(input("Enter the value of temperature: "))
if temperature>30:
    print("It's a hot day")

print(" Have a nice day")'''

# Nested If-else
''' num = int(input("Enter the value of number: "))

if num > 0:
    print("The number is positive")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero") '''

''' num = int(input("Enter the value of number: "))

if num > 0:
    if num % 2 == 0:
        print("The number is positive and even")
    else:
        print("The number is positive and odd")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero") '''

# Check vowel or consonant
'''ch=input(" Enter the Letter ").lower()
if ch in 'aeiou':
    print("Vowel")
else:
    print("Consonant") '''

# Check valid triangle or not
'''a=int(input("The the value of a: "))
b=int(input("The the value of b: "))
c=int(input("The the value of c: "))
if a+b>c and a+c>b and c+b>a:
    print("valid triangle")
else:
    print ("invalid triangle")'''

# loops code
# For loop

'''print(" Print using for loop")
for i in range(1,20):
    print(i)'''

'''fruit=["Mango","banana","Orange","Cherry"]
for i in fruit:
    print(i)'''

# sum of numbers
'''num=[1,2,36,45,50]
total=0
for i in num:
 total+=i
print("Total = ",total)'''

# multipaltion of 5

'''for i in range (1,11):
    print('5*',i,'=',5*i)'''

'''for i in range (1, 50, 5):
    if i == 30:
        break
    print(i)
else:
    print("The number is stopped")'''

'''word=" Data Warehousing"
for i in word:
    print(i)'''

# While Loop

# Counting the Numbers

'''count = 1
while count < 5:
    print (count)
    count += 1'''

#Lab Tasks

#Task1
#1: Write a program that:
#Asks the user to enter a number.
#Checks whether the number is prime number or not using if–else statement.

'''num=input("Enter the number: ")
num=int(num)
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
else:
    print(num,"is not a prime number")'''


#Question 2
#Write a program that:
#Asks the user to enter a number.
#Prints the multiplication table of that number from 1 to 10 using a for loop.

'''num = int(input("Enter the number: "))
for i in range(1, 11):
    print(num, '*', i, '=', num * i)'''


#Question 3
#Write a program that:
#Keeps asking the user to enter a number.
#Stops asking if the user enters 0.
#At the end, prints the sum of all entered numbers (except 0).

'''total = 0
while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num
print("The sum of all entered numbers is:", total)'''








