from robot import Robot
from dinosaur import Dinosaur
Sauron = Dinosaur("Sauron the Great", 20)
Megatron = Robot("Megatron")

class Battlefield:
    def __init__(self,name):
        self.name = name
    def display_welcome(self):
            print(f"Welcome to the {self.name}! Where the futuristic {Megatron.name} will face off against the primal fury of {Sauron.name}!")
            print("")
    def display_winner(self):
        if Megatron.health <= 0:
            print(f"{Sauron.name} is victorious!")
        elif Sauron.health <= 0:
            print(f"{Megatron.name} is victorious!")
    def battle_phase(self):     
        start = input("Are you ready to begin? Yes or No ")
        if start == "Yes" or start == "yes":
            while Megatron.health >= 0 or Sauron.health >= 0:
                Megatron.attack(Sauron)
                if Megatron.health <= 0:
                    print(f"{Megatron.name} has fallen")
                    winner = Sauron.name
                    return winner
                    
                elif Sauron.health <= 0:
                    print(f"{Sauron.name} has fallen")
                    winner = Megatron.name
                    return winner
                    
                Sauron.attack(Megatron)
                if Megatron.health <= 0:
                    print(f"{Megatron.name} has fallen")
                    winner = Sauron.name
                    return winner
                    
                elif Sauron.health <= 0:
                    print(f"{Sauron.name} has fallen")
                    winner = Megatron.name
                    return winner        
        else:
            print("Maybe next time!")
    def run_game(self):
        battlefield.display_welcome()
        battlefield.battle_phase()
        battlefield.display_winner()
       
battlefield = Battlefield("Battleground of Titans")
