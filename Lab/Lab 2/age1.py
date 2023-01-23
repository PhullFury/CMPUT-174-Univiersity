'''
This program compares the inputted age with Frodo's age
Author: Harmanpreet Singh Phull
When: January 19th, 2023
'''

frodo_age = 51

input_name = input("Write the name of the character: ")
input_age = int(input("Write the age of the character: "))

if (input_age <= 0):
    print("Invalid age")
elif (input_age > frodo_age):
    print(input_name, "is", input_age, "years old, and they are older than Frodo.")
elif (frodo_age > input_age):
    print(input_name, "is", input_age, "years old, and they are younger than Frodo.")
elif (frodo_age == input_age):
    print(input_name, "is", input_age, "years old, and they are the same age as Frodo.")