'''
This program takes a user inputed string and multiplys it by a user inputed interger
Author: Harmanpreet Singh Phull
When: January 16th, 2023
'''

phrase = input("Input the phrase: ") 
rep_time = int(input("Input the number of times the phrase is to be repeated: ")) #asking the user about repition time
phrase = phrase + " " #adding a blank space after the phrase 

print(phrase*rep_time) #phrase is multiplied with rep_time to print multiple times