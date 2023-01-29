# the given statement
print("We check in a patient named John Smith \n He's 20 years old and is a new patient")
# create an empty line for spacing
print("\n")
# print us the expected result
print("TASK: Define three variables for \n 1. nae\n 2. age \n 3. check if he's a new or existing patient ")
# create an empty line for spacing
print("\n")
print("My solution:")
# declaring the variables
name = "John Smith"
age = 20
isNew = True


print("The patient name is: " + name)
print("The patient is ",  age, 'years old')
print(isNew)
if(isNew):
    print(name + "is a new patient")
else: print(name + "is an old patient")

print("Make the question a structured")
getName = str(input("what's your name? "))
getAge = int(input("Enter your age: "))
gender = input("Are you a male or female? ")
status = input("Are you a new or old patient: ")

if(gender == "male"):
    gender = "he "
elif (gender == "female"):
    gender = "she "
else: print("(Enter male or female as your gender)")

print("\n")
print("We check in a patient named " + getName + ", \n" + gender + " is ",  getAge, "years old and is a/an " + status + " patient")