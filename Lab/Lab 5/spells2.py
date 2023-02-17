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
    else:
        print("Incorrect!")
        print("The spell was: " + spell)

def main():
    spells = read_spells('spells.txt')
    spell = get_random_spell(spells)
    display_header()
    display_instructions()
    user_input = get_user_input(spell)
    display_feedback(spell, user_input)

main()