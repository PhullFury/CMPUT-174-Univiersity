'''
This program compares the inputted age with characters in the lists
Author: Harmanpreet Singh Phull
When: January 19th, 2023
'''

names = ["Frodo", "Samwise", "Gandalf", "Legolas", "Gimli", "Aragorn", "Boromir", "Merry", "Pippin"]
ages = [51, 39, 2000, 2931, 140, 88, 41, 37, 29]

input_name = input("Write the name of the character: ")
input_age = int(input("Write the age of the character: "))

if (input_age <= 0):
    print("Invalid age")
    quit()  # quits the program early to increase efficiency

young_str = input_name + " is " + str(input_age) + " years old and they are younger than"
old_str = input_name + " is " + str(input_age) + " years old and they are older than"
# initializing strings that are going to be used in the for loop below

first_young = True
first_old = True
# these booleans are used to check if the character being added to the string is the first one or not

for temp_age in ages:
    if (temp_age > input_age):
        temp_age_index = ages.index(temp_age)  # finds the index of the age that was being compared
        temp_name = names[temp_age_index]  # find the character associated with the age being compared
        if (first_young):
            young_str = young_str + " " + temp_name
            first_young = False
        elif (not first_young):
            young_str = young_str + ", " + temp_name
        # the above if and elif are implemented to add a comma only after atleast one character is added to the string
    elif (temp_age < input_age):
        temp_age_index = ages.index(temp_age)
        temp_name = names[temp_age_index]
        if (first_old):
            old_str = old_str + " " + temp_name
            first_old = False
        elif (not first_old):
            old_str = old_str + ", " + temp_name
    elif (temp_age == input_age):
        temp_age_index = ages.index(temp_age)
        temp_name = names[temp_age_index]
        print(input_name + " is " + str(input_age) + " years old and they are the same age as " + temp_name + ".")

if (not first_young):  # only works if first_young is False because not False means True
    print(young_str + ".")
    # only prints if atleast one character is younger than the inputted character
if (not first_old):
    print(old_str + ".")
    # only prints if atleast one character is older than the inputted character
