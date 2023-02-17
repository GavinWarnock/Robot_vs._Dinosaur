from weapon import Weapon

class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = Weapon
    def attack(self, dinosaur):
        dinosaur.health -= active_weapon.attack_power
        print(dinosaur.health)

active_weapon = Weapon("Blaster Cannon", 60)
