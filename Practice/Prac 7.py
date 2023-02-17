import random

def create_board(board_size):
    print("=="*board_size+"=")
    print("|0"*board_size+"|")
    print("=="*board_size+"=")

def roll_die(number_sides):
    return random.randint(1,number_sides)

def main():
    size = int(input("How many squares do you want on the board: "))
    side = int(input("How many sides do you want on your die: "))
    create_board(size)
    print(roll_die(side))
    print("\u2659")

main()