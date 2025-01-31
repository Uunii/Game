## Version 1.0
# Comments, most of the logic works, still need to implement player 2, battle simulation/logic and scoreboard. 
# OOP Principles used: Encapsulation, Inheritance, Polymorphism, Abstraction, static methods

# ----- Idea ------
# Thought process (for me):
# Create a class for character creation
# main function calls class methods
# store selected attributes
# give option to create own class and attributes (work on)
# Create logic for character battle (work on)
# Score board? Multiplayer? (work on)

# Logic flow: Create/Select Charcter -> set attributes -> battle against computer or another player -> keep scoreboard

# Game logic.
# Magic/phsyical resistance, attack type, elemental type, dungeon roguelite archtype game. Loot. 

# Imports ----
import random
from abc import ABC, abstractmethod
from MenuHandler import MenuHandler
from Entities.RaceSelect import RaceSelector, Races
#from Entities.Level_system.Level_logic import Level
from Entities.Level_system.test import Level


# --- Store Characters info ---
MyChar = {}
player2 = {} # not implemented yet
Computer = {}

# ----- Game Entities ---------

class GameCharacter(ABC):
    def __init__(self, name, classification, weapon, defense):
        self.name = name
        self.classification = classification
        self.weapon = weapon
        self.defense = defense

    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def defend(self):
        pass

    def selectCharacter(self):
        MyChar.update({
            "name": self.name,
            "Character type": self.classification,
            "Attack type": self.weapon,
            "Defense type": self.defense
        })

    def Player2(self):
        player2.update({
            "name": self.name,
            "Character type": self.classification,
            "Attack type": self.weapon,
            "Defense type": self.defense
        })

class Companion():
    @staticmethod
    def RandomCharacter():
        random_race = random.choice(Races.racelist[2:])
        Computer.update({
            "Race": random_race
        })
        character_types = ["Warrior", "Wizard"]
        weapons = {
            "Warrior": ["Sword", "Dual Sword"],
            "Wizard": ["Wand", "Dual Wand"]
        }
        attack = {
            "Warrior": ["Sword swing", "Excalibur"],
            "Wizard": ["Summon Lava", "Tornado"]
        }

        char_type = random.choice(character_types)
        chosen_weapon = random.choice(weapons[char_type])
        chosen_attack = random.choice(attack[char_type])

        if char_type == "Warrior":
            if chosen_weapon == "Sword":
                chosen_defense = "Shield"
            elif chosen_weapon == "Dual Sword":
                chosen_defense = None  

        elif char_type == "Wizard":
            if chosen_weapon == "Wand":
                chosen_defense = "Magic Barrier"
            elif chosen_weapon == "Dual Wand":
                chosen_defense = None 

        comp_char = {
            "name": "R3D",
            "Character type": char_type,
            "Attack type": chosen_weapon,
            "Attack": chosen_attack,
            "Defense type": chosen_defense
        }

        Computer.update(comp_char)

        print("\nYour Travel Companion:")
        for key, value in Computer.items():
            print(f"{key}: {value}")


# ------- Character classes ----------

class Warrior(GameCharacter):
    def __init__(self, name):
        super().__init__(name, "Warrior", "Sword", "Shield")

    def attack(self):
        print(f"{self.name} attacks with a {self.weapon}")

    def defend(self):
        print(f"{self.name} defends with a {self.defense}")

    def attack_options(self):
        options = input("Choose Attack: Sword Swing (A), Shield Bash (B), Taunt (C): ").strip().upper()
        return {"A": "Sword Swing", "B": "Shield Bash", "C": "Taunt"}.get(options, "Taunt")

    def defense_options(self):
        options = input("Choose Defense: Shield Guard (A), Run (B): ").strip().upper()
        return {"A": "Shield Guard", "B": "Run"}.get(options, "Run")


class Archer(GameCharacter):
    def __init__(self, name):
        super().__init__(name, "Archer", "Bow", "Dagger")

    def attack(self):
        print(f"{self.name} attacks with a {self.weapon}")

    def defend(self):
        print(f"{self.name} defends witha {self.defense}")
    
    def attack_options(self):
        options = input("Choose Attack options: Fire Arrow(A), Silver arrow(B), Dagger(C): ").strip().upper()
        return {"A": "Fire Arrow", "B": "Silver Arrow", "C": "Dagger"}.get(options, "Dagger")
    
    def dual_offense_options(self):
        options = input("Choose Stronger Offense: Dual Fire Arrows(A), Dual Silver Arrows(B), Dual Dagger(C): ").strip().upper()
        return {"A": "Dual Fire Arrow", "B": "Dual Silver Arrows", "C": "Dual Dagger"}.get(options, "Dagger")
    
    def defense_options(self):
        options = input ("Choose Defense: Dagger throw(A), Run(B): ").strip().upper()
        return {"A": "Dagger", "B": "Run"}.get(options, "Run")
    

class Wizard(GameCharacter):
    def __init__(self, name):
        super().__init__(name, "Wizard", "Wand", "Magic Barrier")

    def attack(self):
        print(f"{self.name} attacks with a {self.weapon}")

    def defend(self):
        print(f"{self.name} defends with a {self.defense}")

    def attack_options(self):
        options = input("Choose Attack Spell: Fireball (A), Ice Shards (B), Domination (C): ").strip().upper()
        return {"A": "Fireball", "B": "Ice Shards", "C": "Domination"}.get(options, "Domination")

    def dual_wand_attack_options(self):
        options = input("Choose Stronger Attack: Enhanced Fireball (A), Lightning Storm (B), Void Blast (C): ").strip().upper()
        return {"A": "Enhanced Fireball", "B": "Lightning Storm", "C": "Void Blast"}.get(options, "Void Blast")

    def defense_spells(self):
        options = input("Choose Defensive Spell: FireWall (A), IceWall (B), Run (C): ").strip().upper()
        return {"A": "FireWall", "B": "IceWall", "C": "Run"}.get(options, "Run")


class Assassin(GameCharacter ):
    def __init__(self, name):
        super().__init__(name, "Assassin", "Daggers", "Stealth Cloak")

    def attack(self):
        print(f"{self.name} attacks with a {self.weapon}")
    def defend(self):
        print(f"{self.name} hides with {self.defense}")
    
    def attack_options(self):
        options = input("Choose Attack: Stab (A), Shuriken (B), Poison Darts (C): ").strip().upper()
        return {"A": "Stab", "B": "Shuriken", "C": "Poison Darts"}.get(options, "Poison Darts")
    
    def defense_options(self):
        options = input("Choose Defense: Stealth Cloak (A), Run(B)")
        return {"A": "Stealth Cloak", "B": "Run"}.get(options, "Run")
    

# ---- create character ------
def create_character():
    name = input("Enter your character name: ")
    Raceselected = RaceSelector()
    MyChar.update({
        "Race": Raceselected
    })
    character_select = MenuHandler("Characters")
    character_select.format_menu()
    choice = MenuHandler.choice()

    if choice == 1:  
        wizard = Wizard(name)
        wizard_data = {"name": wizard.name, "Character type": wizard.classification}
        MyChar.update(wizard_data)

        wizard_weapon_menu = MenuHandler("Wizard Weapon")
        wizard_weapon_menu.format_menu()
        weapon_choice = MenuHandler.choice()

        if weapon_choice == 1:
            wizard.weapon = "Wand"
            wizard.defense = "Magic Barrier"
        elif weapon_choice == 2:
            wizard.weapon = "Dual Wand"
            wizard.defense = None

        wizard_data.update({
            "Attack type": wizard.weapon,
            "Defense type": wizard.defense
        })

        if wizard.weapon == "Wand":
            wizard_spell = wizard.attack_options()
            wizard_defense = wizard.defense_spells()
            wizard_data.update({
                "Chosen attack": wizard_spell,
                "Chosen defense": wizard_defense
            })
        elif wizard.weapon == "Dual Wand":
            wizard_spell = wizard.dual_wand_attack_options()
            wizard_data.update({
                "Chosen attack": wizard_spell
            })

        MyChar.update(wizard_data)

    elif choice == 2:  
        warrior = Warrior(name)
        warrior_data = {"name": warrior.name, "Character_type": warrior.classification}
        MyChar.update(warrior_data)

        warrior_weapon_menu = MenuHandler("Warrior Weapon")
        warrior_weapon_menu.format_menu()
        weapon_choice = MenuHandler.choice()

        if weapon_choice == 1:
            warrior.weapon = "Sword"
            warrior.defense = "Shield"
        elif weapon_choice == 2:
            warrior.weapon = "Dual Sword"
            warrior.defense = None

        warrior_data.update({
            "Attack type": warrior.weapon,
            "Defense type": warrior.defense
        })

        warrior_attack = warrior.attack_options()
        warrior_defense = warrior.defense_options()
        warrior_data.update({
            "Chosen attack": warrior_attack,
            "Chosen defense": warrior_defense
        })
        MyChar.update(warrior_data)

    elif choice == 3:
        archer = Archer(name)
        archer_data = {"name": archer.name, "Character_type": archer.classification}
        MyChar.update(archer_data)

        archer_weapon_menu = MenuHandler("Archer Weapon")
        archer_weapon_menu.format_menu()
        weapon_choice = MenuHandler.choice()

        if weapon_choice == 1:
            archer.weapon = "Arrow"
            archer.Defense = "Dagger"
        elif weapon_choice == 2:
            archer.weapon = "Dual Arrows"
            archer.defense = None

        archer_data.update({
            "Attack type": archer.weapon,
            "Defense type": archer.defense
        })

        archer_attack = archer.attack_options()
        archer_defense = archer.defense_options()
        archer_data.update({
            "Chose attack": archer_attack,
            "Chosen defense": archer_defense
        })
        MyChar.update(archer_data)


    player_level = Level()
    MyChar.update({
        "Current Level": player_level.get_level()
    })
    MyChar.update({
        "xp": {
            "Experience (xp)": 0,
            "Xp needed to level up": 10
        }
    })
    
    
# ------- Main ---------
def Player_entity():
    start = MenuHandler("Start")
    start.format_menu()
    choice = MenuHandler.choice()

    if choice == 1:
        create_character()
    elif choice == 2:
        Companion.RandomCharacter()

    return MyChar

