#import the date package to use it in this program
from datetime import  date


# the task question
print("Write a program that calculate the age of the user")
# display the current time/date
print("Today date: ", date.today())
# print the current year
print(date.today().year)
#print the current month
print(date.today().month)
#print the current day
print(date.today().day)


print("A PROGRAM THAT CALCULATE THE USER'S CURRENT AGE")
# get the user age
getBirthDate = int(input("Enter your YEAR OF BIRTH (e.g. 1994, 2002): "))
birthDate = (date.today().year - getBirthDate)
# print the user age
print("You are ", birthDate, "years old")
