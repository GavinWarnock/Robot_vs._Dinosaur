from robot import Robot
from dinosaur import Dinosaur


class Battlefield:
    def __init__(self,name):
        self.dinosaur_one = Dinosaur("Sauron the Great", 20)
        self.robot_one = Robot("Megatron")
        self.name = name
    def display_welcome(self):
            print(f"Welcome to the {self.name}! Where the futuristic {self.robot_one.name} will face off against the primal fury of {self.dinosaur_one.name}!")
            print("")
    def display_winner(self):
        if self.robot_one.health <= 0:
            print(f"{self.dinosaur_one.name} is victorious!")
        elif self.dinosaur_one.health <= 0:
            print(f"{self.robot_one.name} is victorious!")
    def battle_phase(self):     
        start = input("Are you ready to begin? Yes or No ")
        if start == "Yes" or start == "yes":
            while self.robot_one.health >= 0 or self.dinosaur_one.health >= 0:
                self.robot_one.attack(self.dinosaur_one)
                if self.robot_one.health <= 0:
                    print(f"{self.robot_one.name} has fallen")
                    winner = self.dinosaur_one.name
                    break
                    
                elif self.dinosaur_one.health <= 0:
                    print(f"{self.dinosaur_one.name} has fallen")
                    winner = self.robot_one.name
                    break
                    
                self.dinosaur_one.attack(self.robot_one)
                if self.robot_one.health <= 0:
                    print(f"{self.robot_one.name} has fallen")
                    winner = self.dinosaur_one.name
                    break
                    
                elif self.dinosaur_one.health <= 0:
                    print(f"{self.dinosaur_one.name} has fallen")
                    winner = self.robot_one.name
                    break        
        else:
            print("Maybe next time!")
    def run_game(self):
        battlefield.display_welcome()
        battlefield.battle_phase()
        battlefield.display_winner()
       
battlefield = Battlefield("Battleground of Titans")
