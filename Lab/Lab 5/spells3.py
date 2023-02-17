import random

def display_header():
    print('############################################################')
    print('Harry Potter Keyboard Trainer')
    print('############################################################')

def display_instructions():
    with open('instructions.txt', 'r') as file:
        line = file.readline().rstrip('\n')
        while not line == "":
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
    random_index = random.randint(0, len(list)-1)
    spell = list[random_index].lower()
    return spell

def get_user_input(spell):
    print("Type the following spell: " + spell)
    return input("")

def display_feedback(spell, user_input):
    if (spell == user_input):
        print("Correct!")
        return 10
    else:
        print("Incorrect!")
        print("The spell was: " + spell)
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
        score += display_feedback(spell, user_input)
        choice_bool = play_again()
    print("Thanks for playing.")
    print("Final Score: " + str(score))

main()