# Enemies for game
from abc import ABC, abstractmethod
from Topi_Game.MenuHandler import MenuHandler
import random

enemy_Computer = {}


class GameEnemies(ABC):
    def __init__(self, name, classification, weapon, defense):
        self.name = name
        self.classification = classification
        self.weapon = weapon 
        self.defense = defense
        #self.health = health

    @abstractmethod
    def attack(self):
        pass
    
    @abstractmethod
    def defense(self):
        pass
        

    @staticmethod
    def RandomEnemy():
        enemy_types = ["Goblin", "Wolf"]
        weapons = {
            "Goblin": ["Dagger", "Dual Dagger"],
            "Wolf": ["Canine", "Pack Hunt"]
        }
        attack = {
            "Goblin": ["Stab", "Stealh"],
            "Wolf": ["Bite", "Stealth hunt"]
        }
        char_type = random.choice(enemy_types)
        chosen_weapon = random.choice(weapons[char_type])
        chosen_attack = random.choice(attack[char_type])

        if char_type == "Goblin":
            if chosen_weapon == "Dagger":
                chosen_defense = "Bite"
            elif chosen_weapon == "Dual Dagger":
                chosen_defense = "Dagger throw"
            
        elif char_type == "Wolf":
            if chosen_weapon == "Canine":
                chosen_defense = "Latch"
            elif chosen_weapon == "Pack Hunt":
                chosen_defense = "Call of the pack"

        enemy_comp_char = {
            "name" : f"{chosen_weapon} {char_type} ",
            "Character_type": char_type,
            "Attack_type": chosen_weapon,
            "Attack": chosen_attack,
            "Defense_type": chosen_defense,
        }

        enemy_Computer.update(enemy_comp_char)
        print("------------------------------------")
        print(f"The enemy {char_type} has spawned")
        print(f"The {char_type} stats:")
        for key, value in enemy_Computer.items():
            print(f"{key} : {value}")
        print("------------------------------------")

def main():
    start = MenuHandler("Start")
    start.format_menu()
    choice = MenuHandler.choice()

    if choice == 1:
        Max_enemies = random.randrange(1, 10, 1)
        for i in range(Max_enemies):
            print(f"\nEnemy {i+1}")
            GameEnemies.RandomEnemy()
    
main()
