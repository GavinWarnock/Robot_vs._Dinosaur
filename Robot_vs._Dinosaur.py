from robot import Robot
from dinosaur import Dinosaur
from weapon import Weapon
active_weapon = Weapon("Blaster Cannon", 60)
Sauron = Dinosaur("Sauron the Great", 50)
Megatron = Robot("Megatron")

Sauron.attack(Megatron)
Megatron.attack(Sauron)