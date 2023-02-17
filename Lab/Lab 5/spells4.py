'''
This program read spells from a file and checks the user's typing speed
Name: Harmanpreet Singh Phull
Date: 16th February 2023
'''
import random
import time

def display_header():
    print('############################################################')
    print('Harry Potter Keyboard Trainer')
    print('############################################################')

def display_instructions():
    with open('instructions.txt', 'r') as file:
        line = file.readline().rstrip('\n')
        while not line == "":  # loops until the file ends
            print(line)
            line = file.readline().rstrip('\n')

def read_spells(filename):
    spells = []
    with open(filename, 'r') as file:
        line = file.readline()
        while not line == "":
            spells.append(line.rstrip("\n"))
            line = file.readline()
    return spells

def get_random_spell(list):
    random_index = random.randint(0, len(list)-1)  # finds a random index
    spell = list[random_index].lower()
    return spell

def get_user_input(spell):
    start = time.time()
    print('Type the following spell: ' + spell)
    user_input = input().lower()  # converts the user's input to lower so that there is no problem while comparing
    user_time = round(time.time() - start, 2)
    print("Result: " + str(user_time) + " seconds (goal: " + str(get_target_time(spell)) + " seconds).")
    return user_input, user_time  # returns a list

def get_target_time(spell):
    return len(spell) * 0.3

def calculate_points(spell, user_input, user_time):
    target_time = get_target_time(spell)
    if (spell == user_input):
        if (user_time <= target_time):
            print("You get 10 points!")
            return 10
        elif (target_time < user_time <= target_time*1.5):
            print("You got 6 points!")
            return 6
        elif (target_time*1.5 < user_time <= target_time*2):
            print("You got 3 points!")
            return 3
        elif (target_time*2 <user_time):
            print("You got 1 points!")
            return 1
    else:
        print("You got -5 points!")
        return -5

def play_again():
    choice = input("Do you want to continue? (y/n): ").lower()
    if (choice == "y"):
        return True
    elif (choice == "n"):
        return False

def main():
    spells = read_spells('spells.txt')
    display_header()
    display_instructions()

    score = 0
    choice_bool = True
    while choice_bool:
        spell = get_random_spell(spells)
        user_input = get_user_input(spell)
        score += calculate_points(spell, user_input[0], user_input[1])  # is used to get different values from user_input list
        choice_bool = play_again()
    print("\n" + "Thanks for playing.")
    print("Final Score: " + str(score))

main()