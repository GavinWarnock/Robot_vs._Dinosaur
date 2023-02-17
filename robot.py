from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = [Weapon("Blaster Cannon", 40), Weapon("Beam Sword", 20), Weapon("Fists", 10)] 
    def attack(self, dinosaur):
        weapon_choice = input("Choose your weapon! Blaster Cannon, Beam Sword, or Fists ")
        if weapon_choice == "Blaster Cannon":
            dinosaur.health -= self.active_weapon[0].attack_power
            print(f"{self.name} has struck {dinosaur.name} with his {self.active_weapon[0].name} for {self.active_weapon[0].attack_power} damage!")
            print(f"{dinosaur.name} has {dinosaur.health} health remaining!")
        elif weapon_choice == "Beam Sword":
            dinosaur.health -= self.active_weapon[1].attack_power
            print(f"{self.name} has struck {dinosaur.name} with his {self.active_weapon[1].name} for {self.active_weapon[1].attack_power} damage!")
            print(f"{dinosaur.name} has {dinosaur.health} health remaining!") 
        elif weapon_choice == "Fists":
            dinosaur.health -= self.active_weapon[2].attack_power
            print(f"{self.name} has struck {dinosaur.name} with his {self.active_weapon[2].name} for {self.active_weapon[2].attack_power} damage!")
            print(f"{dinosaur.name} has {dinosaur.health} health remaining!")