import random

class Pokemon:
    def __init__(self, name, attack, defense, max_health, current_health):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.max_health = max_health
        self.current_health = current_health

    def __str__(self):
        return f"{self.name} (health: {self.current_health}/{self.current_health})"

    def lose_health(self, amount):
        if (amount >= 0):
            if (amount > self.max_health):
                self.current_health = 0
            else:
                self.current_health = self.current_health - amount

    def is_alive(self):
        if (self.current_health <= 0):
            return False
        else:
            return True

    def revive(self):
        self.current_health = self.max_health


def read_pokemon_from_file(filename):
    with open(filename, "r", encoding="utf-8") as file:
        str = file.readline()
        str = file.readline().rstrip("\n")
        mon_list = []
        while not str == "":
            name = str[:str.find("|")]
            temp1 = str[str.find("|") + 1:]
            attack = temp1[:temp1.find("|")]
            temp2 = temp1[temp1.find("|") + 1:]
            defense = temp2[:temp2.find("|")]
            temp3 = temp2[temp2.find("|") + 1:]
            health = temp3
            temp_mon = Pokemon(name, int(attack), int(defense), int(health), int(health))
            mon_list.append(temp_mon)
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
        return two_mon


def main():
    mon_list = read_pokemon_from_file("all_pokemon.txt")
    pokemon1 = mon_list[0]
    pokemon2 = mon_list[1]
    print(f"Welcome, {pokemon1} and {pokemon2}!")

if __name__ == "__main__":
    main()