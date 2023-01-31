'''
This program checks whether the inputted word is the correct Klingon word
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

guess = input("Translate computer into Klingon: ")

if (guess == Klingon[2]):
    print("Correct")
else:
    print("Sorry, you're wrong!")
    print("The correct answer is", Klingon[2])