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


def main():
    pokemon1 = Pokemon("Pikachu", 55, 40, 35, 35)
    pokemon2 = Pokemon("Bulbasaur", 49, 49, 45, 45)
    print(f"Welcome, {pokemon1} and {pokemon2}!")


if __name__ == "__main__":
    main()