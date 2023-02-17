from robot import Robot
from dinosaur import Dinosaur
from herd import Herd
from fleet import Fleet
import random
class Battlefield:
    def __init__(self,name):
        self.dinosaur = None
        self.robot = None
        self.herd = Herd()
        self.fleet = Fleet()
        self.name = name

    def pick_random_dino(self,):
        selected_dino = random.choice(self.herd.dino_herd)
        self.dinosaur = selected_dino
        print(selected_dino.name)
        return selected_dino
    def pick_random_robot(self,):
        selected_robot = random.choice(self.fleet.robot_fleet)
        self.robot = selected_robot
        print(selected_robot.name)
        return selected_robot
        

    def display_welcome(self):
        battlefield.pick_random_robot()
        battlefield.pick_random_dino()
        print(f"Welcome to the {self.name}! Where the futuristic {self.robot.name} will face off against the primal fury of {self.dinosaur.name}!")
        print("")
    def display_winner(self):
        if self.robot.health <= 0:
            print(f"{self.dinosaur.name} is victorious!")
        elif self.dinosaur.health <= 0:
            print(f"{self.robot.name} is victorious!")
    def battle_phase(self):     
        start = input("Are you ready to begin? Yes or No ")
        if start == "Yes" or start == "yes":
            while self.robot.health >= 0 or self.dinosaur.health >= 0:
                self.robot.attack(self.dinosaur)
                if self.robot.health <= 0:
                    print(f"{self.robot.name} has fallen")
                    winner = self.dinosaur.name
                    break
                    
                elif self.dinosaur.health <= 0:
                    print(f"{self.dinosaur.name} has fallen")
                    winner = self.robot.name
                    break
                    
                self.dinosaur.attack(self.robot)
                if self.robot.health <= 0:
                    print(f"{self.robot.name} has fallen")
                    winner = self.dinosaur.name
                    break
                    
                elif self.dinosaur.health <= 0:
                    print(f"{self.dinosaur.name} has fallen")
                    winner = self.robot.name
                    break        
        else:
            print("Maybe next time!")
    def run_game(self):
        battlefield.display_welcome()
        battlefield.battle_phase()
        battlefield.display_winner()
       
battlefield = Battlefield("Battleground of Titans")
