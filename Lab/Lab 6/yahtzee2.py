'''
This program plays a simplified version of the board game 'Yahtzee'
Name: Harmanpreet Singh Phull
Date: 8th March 2023
'''

import random

def make_roll():
    roll_info = []
    for i in range(5):  # loops five times
        roll_info.append(random.randint(1,6))  # picks any random number between 1 and 6 and adds it the list
    return tuple(roll_info)  # converts the list to a tuple

def sum_of_given_number(roll: tuple, number: int):
    sum = 0
    for i in roll:
        if (i == number):
            sum += number
    return sum

def fill_upper_section(roll: tuple):
    sum_info = []
    for i in range(1,7):  # starts from 1 and goes till 6
        sum_info.append(sum_of_given_number(roll,i))
    return sum_info

def display_upper_section(upper_section_scores: list):  # displays the list by printing different indexes in the different lines
    print("Aces: " + str(upper_section_scores[0]))
    print("Twos: " + str(upper_section_scores[1]))
    print("Threes: " + str(upper_section_scores[2]))
    print("Fours: " + str(upper_section_scores[3]))
    print("Fives: " + str(upper_section_scores[4]))
    print("Sixes: " + str(upper_section_scores[5]))

def num_of_a_kind(roll: tuple, number: int):
    sum_info = fill_upper_section(roll)  # gets the filled upper section list
    counter = 1
    req_met = False
    for i in sum_info:
        if (i == counter*number):   # loops through the entire list
            req_met = True
        counter += 1

    if req_met:
        sum = 0
        for x in sum_info:
            sum += x
        return sum
    else:
        return 0

def yahtzee(roll: tuple):
    if (roll[0] == roll[1] == roll[2] == roll[3] == roll[4]):  # checks whether all indexes have the same value
        return 50
    else:
        return 0

def main():
    roll = make_roll()
    print("Rolling the dice... " + str(roll))
    print("Upper Section: ")
    display_upper_section(fill_upper_section(roll))
    print("\nLower Section: ")  # '\n' starts a new line for ease of reading
    print("Three of a kind: " + str(num_of_a_kind(roll,3)))
    print("Four of a kind: " + str(num_of_a_kind(roll,4)))
    print("Yahtzee: " + str(yahtzee(roll)))

if __name__ == "__main__":
    main()