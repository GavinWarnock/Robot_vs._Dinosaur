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
            
                
    def run_game(self):
        battlefield.display_welcome()
        start = input("Are you ready to begin? Yes or No ")
        if start == "Yes":
            while Megatron.health >= 0 or Sauron.health >= 0:
                Megatron.attack(Sauron)
                if Megatron.health <= 0:
                    print(f"{Megatron.name} has fallen, {Sauron.name} wins!")
                    break
                elif Sauron.health <= 0:
                    print(f"{Sauron.name} has fallen {Megatron.name} wins!")
                    break
                Sauron.attack(Megatron)
                if Megatron.health <= 0:
                    print(f"{Megatron.name} has fallen, {Sauron.name} wins!")
                    break
                elif Sauron.health <= 0:
                        print(f"{Sauron.name} has fallen {Megatron.name} wins!")
                        break
        else:
            print("Maybe next time!")


battlefield = Battlefield("Battleground of Titans")
