'''
This program asks the user for a constant and then checks if the inputted word is correct or not and gives a hint if wrong
Name: Harmanpreet Singh Phull
Date: 31st January 2023
'''

import random

with open("klingon-english.txt", "r") as File:
    Klingon = []
    English = []
    line = File.readline()
    index = line.find("|")  # finds the index of "|" because it separates the English and Klingon words
    while not line == "":  # loops until the line is empty
        Klingon.append(line[:index])
        English.append(line[index + 1:].rstrip("\n"))  # removes \n from the English words
        line = File.readline()
        index = line.find("|")

valid_cons = False
while not valid_cons:  # loops until a correct constant is found
    cons = input("Type the Klingon constant you want to work with: ")
    for temp in Klingon:
        index_cons = temp.find(cons)  # find the index of the user inputted constant
        if (index_cons == 0):  # only works if the user inputted constant is at index 0
            valid_cons = True
            index_word = Klingon.index(temp)
    if (not valid_cons):
        print("Not a valid Klingon constant.\n")

Klingon_word = Klingon[index_word]
Klingon_sub = Klingon_word[1:len(Klingon_word) - 1]  # gets the substring that doesn't include the first and last character
hint1 = Klingon_word.replace(Klingon_sub, "*" * len(Klingon_sub))  # replaces that substring with *

index_rand = random.randint(1, len(Klingon_word) - 2)  # gets a random index between the first and last character
temp_list = list(hint1)  # converts hint1 into a list as strings are immutable
temp_list[index_rand] = Klingon_word[index_rand]  # replaces one * with an actual letter
hint2 = "".join(temp_list)  # converts the list into a string

guess_number = 1
got_answer = False
while guess_number <= 3 and not got_answer:  # loops until an answer is found or 3 guesses are made
    guess = input("Translate " + English[index_word] + " into Klingon: ")
    if (guess == Klingon_word):
        got_answer = True
    elif (not guess == Klingon_word and not guess_number == 3):
        print("Not quite there!")
        if (guess_number == 1):
            print("Here's a hint: " + hint1 + "\n")
        elif (guess_number == 2):
            print("Here's a hint: " + hint2 + "\n")
    guess_number += 1

if (got_answer):
    print("Correct")
elif (not got_answer):
    print("Sorry, you're wrong!")
    print("The correct answer is " + Klingon[index_word])