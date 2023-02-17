import random

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

def main():
    filename = input("Write the name of the file: ")
    spells = read_spells(filename)
    print('Harry Potter Keyboard Trainer')
    spell = get_random_spell(spells)
    print(spell)

main()