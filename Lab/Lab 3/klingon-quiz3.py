'''
This program asks the user for a constant and then checks if the inputted word is correct or not and gives a hint if wrong
Name: Harmanpreet Singh Phull
Date: 31st January 2023
'''

with open("klingon-english.txt", "r") as File:
    Klingon = []
    English = []
    line = File.readline()
    index = line.find("|")
    while not line == "":
        Klingon.append(line[:index])
        English.append(line[index + 1:].rstrip("\n"))
        line = File.readline()
        index = line.find("|")

valid_cons = False
while not valid_cons:
    cons = input("Type the Klingon constant you want to work with: ")
    for temp in Klingon:
        index_cons = temp.find(cons)
        if (index_cons == 0):
            valid_cons = True
            index_word = Klingon.index(temp)
    if (not valid_cons):
        print("Not a valid Klingon constant.\n")

guess_number = 1
got_answer = False
Klingon_word = Klingon[index_word]
Klingon_sub = Klingon_word[1:len(Klingon_word)-1]
hint = Klingon_word.replace(Klingon_sub,"*"*len(Klingon_sub))
while guess_number <= 3 and not got_answer:
    guess = input("Translate " + English[index_word] + " into Klingon: ")
    if (guess == Klingon_word):
        got_answer = True
    elif (not guess == Klingon_word and not guess_number == 3):
        print("Not quite there!")
        print("Here's a hint: " + hint + "\n")
    guess_number += 1


if (got_answer):
    print("Correct")
elif (not got_answer):
    print("Sorry, you're wrong!")
    print("The correct answer is " + Klingon[index_word])