import random

def make_roll():
    roll_info = []
    for i in range(5):
        roll_info.append(random.randint(1,6))
    return tuple(roll_info)

def sum_of_given_number(roll: tuple, number: int):
    sum = 0
    for i in roll:
        if (i == number):
            sum += number
    return sum

def fill_upper_section(roll: tuple):
    sum_info = []
    for i in range(1,7):
        sum_info.append(sum_of_given_number(roll,i))
    return sum_info

def display_upper_section(upper_section_scores: list):
    print("Aces: " + str(upper_section_scores[0]))
    print("Twos: " + str(upper_section_scores[1]))
    print("Threes: " + str(upper_section_scores[2]))
    print("Fours: " + str(upper_section_scores[3]))
    print("Fives: " + str(upper_section_scores[4]))
    print("Sixes: " + str(upper_section_scores[5]))

def main():
    roll = make_roll()
    print("Rolling the dice... " + str(roll))
    print(fill_upper_section(roll))
    print("Upper Section: ")
    display_upper_section(fill_upper_section(roll))

if __name__ == "__main__":
    main()