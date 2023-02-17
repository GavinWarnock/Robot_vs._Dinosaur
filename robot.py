from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon("Blaster, Cannon", 40)
    def attack(self, dinosaur):
        dinosaur.health -= self.active_weapon.attack_power
        print(f"{self.name} has blasted {dinosaur.name} with his {self.active_weapon.name} for {self.active_weapon.attack_power} damage!")
        print(f"{dinosaur.name} has {dinosaur.health} health remaining!")
        
