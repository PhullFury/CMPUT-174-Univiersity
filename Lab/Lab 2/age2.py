'''
This program compares the inputted age with Frodo's and Gollum' age
Author: Harmanpreet Singh Phull
When: January 19th, 2023
'''

frodo_age = 51
gollum_age = 589

input_name = input("Write the name of the character: ")
input_age = int(input("Write the age of the character: "))

if (input_age <= 0):
    print("Invalid age")
elif (input_age > frodo_age and input_age > gollum_age):
    print(input_name, "is", input_age, "years old, and they are older than Gollum and Frodo.")
elif (input_age > frodo_age and input_age < gollum_age):
    print(input_name, "is", input_age, "years old, and they are older than Frodo but younger than Gollum.")
elif (input_age < frodo_age and input_age < gollum_age):
    print(input_name, "is", input_age, "years old, and they are younger than Gollum and Frodo.")