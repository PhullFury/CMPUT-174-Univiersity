'''
This program compares the inputted age with Pippin's, Frodo's, Gollum's and Arwen's age
Author: Harmanpreet Singh Phull
When: January 19th, 2023
'''

pippin_age = 29
frodo_age = 51
gollum_age = 589
arwen_age = 2901

input_name = input("Write the name of the character: ")
input_age = int(input("Write the age of the character: "))

if (input_age <= 0):
    print("Invalid age")
elif (input_age > pippin_age and input_age > frodo_age and input_age > gollum_age and input_age > arwen_age):
    print(input_name, "is", input_age, "years old, and they are older than Arwen, Gollum, Frodo, Pippin.")
elif (input_age > pippin_age and input_age > frodo_age and input_age > gollum_age):
    print(input_name, "is", input_age, "years old, and they are older than Gollum, Frodo, Pippin.")
    if (input_age < arwen_age):
        print(input_name, "is", input_age, "years old, and they are younger than Arwen.")
    elif (input_age == arwen_age):
        print(input_name, "is", input_age, "years old, and they are the same age as Arwen.")
elif (input_age > pippin_age and input_age > frodo_age and input_age < arwen_age):
    print(input_name, "is", input_age, "years old, and they are older than Pippin, Frodo.")
    if (input_age < gollum_age):
        print(input_name, "is", input_age, "years old, and they are younger than Arwen, Gollum.")
    elif (input_age == gollum_age):
        print(input_name, "is", input_age, "years old, and they are younger than Arwen but the same age as Gollum.")
elif (input_age > pippin_age and input_age < gollum_age and input_age < arwen_age):
    print(input_name, "is", input_age, "years old, and they are older than Pippin.")
    if (input_age < frodo_age):
        print(input_name, "is", input_age, "years old, and they are younger than Arwen, Gollum, Frodo.")
    elif (input_age == frodo_age):
        print(input_name, "is", input_age, "years old, and they are younger than Arwen, Gollum but the same age as Frodo.")
elif (input_age < frodo_age and input_age < gollum_age and input_age < arwen_age):
    if (input_age < pippin_age):
        print(input_name, "is", input_age, "years old, and they are younger than Arwen, Gollum, Frodo, Pippin.")
    elif (input_age == pippin_age):
        print(input_name, "is", input_age, "years old, and they are younger than Arwen, Gollum, Frodo but the same age as Pippin.")