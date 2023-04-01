import random

class Pokemon:
    def __init__(self, name, attack, defense, max_health, current_health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.current_health = current_health
        # initiates the base attributes of pokemon

    def __str__(self):
        return f"{self.name} (health: {self.current_health}/{self.max_health})"
        # returns a string representation of pokemon

    def lose_health(self, amount):
        if (amount >= 0):  # checks whether the damage is greater than 0
            if (amount > self.current_health):
                self.current_health = 0
                # if the damage is greater than the current health the health is directly set to 0 so the health doesn't become negative
            else:
                self.current_health -= amount

    def is_alive(self):
        if (self.current_health <= 0):  # checks whether the pokemon's health is zero or lower
            return False
        else:
            return True

    def revive(self):
        chance = random.randint(1,10)  # gets a random number
        if (chance >= 6):
            self.current_health = self.max_health
            print(f"{self.name} revived!")
        else:
            print(f"{self.name} attempted a revive, but failed!")
        # there's a fifty percent chance that the pokemon would revive

    def attempt_attack(self, other: "Pokemon"):
        return round(self.attack*random.randint(7,13)/10)
        # gets the round value of the modified attack


def read_pokemon_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        str = file.readline()  # removes the first line from the line
        str = file.readline().rstrip("\n")
        mon_list = []
        while not str == "":  # runs until the file is completely looped
            name = str[:str.find("|")]
            temp1 = str[str.find("|") + 1:]
            attack = temp1[:temp1.find("|")]
            temp2 = temp1[temp1.find("|") + 1:]
            defense = temp2[:temp2.find("|")]
            temp3 = temp2[temp2.find("|") + 1:]
            health = temp3
            # strips and gets different values from each line of file
            temp_mon = Pokemon(name, int(attack), int(defense), int(health), int(health))  # initiates pokemon
            mon_list.append(temp_mon)  # adds the pokemon to the list
            str = file.readline().rstrip("\n")
        two_mon = []
        counter = 0
        while not len(two_mon) == 2:
            index = random.randint(0,len(mon_list)-1)
            if (counter > 0):
                if (not two_mon[0] == mon_list[index]):
                    two_mon.append(mon_list[index])
            else:
                two_mon.append(mon_list[index])
            counter += 1
        # gets two random pokemon from the list
        return two_mon


def main():
    mon_list = read_pokemon_from_file("all_pokemon.txt")
    pokemon1 = mon_list[0]  # gets the first pokemon from list
    pokemon2 = mon_list[1]  # gets the second pokemon from list
    print(f"Welcome, {pokemon1} and {pokemon2}!")
    win = False
    for round in range(1,11):  # runs for 10 rounds
        print(f"\nRound {round} begins! {pokemon1} and {pokemon2}")
        p1_attack = pokemon1.attempt_attack(pokemon2)  # the first pokemon attempts attacks
        print(f"{pokemon1.name} attempts an attack on {pokemon2.name} for {p1_attack} damage!")
        if (p1_attack > pokemon2.defense):  # checks whether the attack is greater than the defense
            pokemon2.lose_health(p1_attack)  # pokemon 2 loses heath
            print(f"Attack was successful! {pokemon2.name} has {pokemon2.current_health} health remaining!")
            if (not pokemon2.is_alive()):  # pokemon 2 tries to revive if it dies
                pokemon2.revive()
        else:
            print("Attack is blocked!")
        if (not pokemon2.is_alive()):  # if pokemon 2 is dead pokemon 1 wins
            print(f"\n{pokemon1} has won in {round} rounds!")
            win = True
            break
        p2_attack = pokemon2.attempt_attack(pokemon1)
        print(f"{pokemon2.name} attempts an attack on {pokemon1.name} for {p2_attack} damage!")
        if (p2_attack > pokemon1.defense):
            pokemon1.lose_health(p2_attack)
            print(f"Attack was successful! {pokemon1.name} has {pokemon1.current_health} health remaining!")
            if (not pokemon1.is_alive()):
                pokemon1.revive()
        else:
            print("Attack is blocked!")
        if (not pokemon1.is_alive()):
            print(f"\n{pokemon2} has won in {round} rounds!")
            win = True
            break
        # same logic as the 1st pokemon but reversed
    if (not win):  # if no one wins after 10 rounds both pokemon are tied
        print(f"\nIt's a tie between {pokemon1} and {pokemon2}!")


if __name__ == "__main__":
    main()