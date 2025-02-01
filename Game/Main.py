## Version 1.2
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

import json
from Entities.Player_entity import Player_entity
from Entities.Enemy_entity import Enemy_entity
from Entities.Level_system.Level_logic import Level
from Entities.Level_system.Xp_points import ExperienceManager  
from Entities.Level_system.Skill_points  import SkillPoints

filename = "Game/Entities/SaveData/Player.json"

Player1 = {}

def update_data():
    
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        return {}

def save_data(data):
    
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"Error saving data: {e}")

def reset_data():
   
    with open(filename, 'w') as f:
        f.write("")

def first_save(data):

    if "Player" not in data:
        data["Player"] = {}
    
    if "Current Level" not in data["Player"]:
        data["Player"]["Current Level"] = {"Level": 0, "Skill Points": 0}

    save_data(data)

def Save_level():
    
    player_level = Level()
    player_level.level_up()
    Player1.setdefault("Current Level", {"Level": 0, "Skill Points": 0})
    Player1["Current Level"]["Level"] = player_level.get_level()
    save_data(Player1)

def Reset_level():
  
    player_level = Level()
    player_level.reset_level()
    Player1.setdefault("Current Level", {"Level": 0, "Skill Points": 0})
    Player1["Current Level"]["Level"] = player_level.get_level()
    save_data(Player1)

def print_player_data(player_data):
    for key, val in player_data.items():
        print(f"🔹 {key}:")  
        if isinstance(val, dict):
            for sub_key, sub_val in val.items():
                if sub_key == "Race":
                    print(f"  - Race: {sub_val["Name"]}")
                elif sub_key != "xp" and sub_key != "Current Level":  
                    if isinstance(sub_val, dict):  
                        print(f"  ➡️ {sub_key}:")
                    else:
                        print(f"  ➡️ {sub_key}: {sub_val}")
            print("🟩" * 15)  # 
        else:
            print(f"  {val}")
        print()  
def display_xp(player):
    xp_info = player.get("Player", {}).get("xp", {})
    current_level_info = player.get("Player", {}).get("Current Level", {})
    if xp_info and current_level_info:
        experience = xp_info.get('Experience (xp)', 0)
        xp_needed = xp_info.get('Xp needed to level up', 10)  
        level = current_level_info.get("Level", 0)
        skill_points = current_level_info.get("Skill Points", 0)
        print("🎮 --- Lvl Status --- 🎮")
        print(f"🔸 Current Level: {level}")
        print(f"🔸 Skill Points: {skill_points}")
        print(f"🔸 XP: {experience}/{xp_needed}")
        print("🔶" * 15) 
    else:
        print("No XP info available.")
        print("🔶" * 15)  

def main():
    global Player1
    print("\n --- Welcome to the game! ---\n")
    
    if not Player1:
        print("Would you like to load from a previous save?\n")
        option = input("Enter choice (y/n): ").lower() 
        if option == 'y':
            previous_save = update_data()  
            if previous_save:
                Player1.update(previous_save)
                print("\n------ 🟢 Current Save 🟢 ----------\n")
                print_player_data(Player1)
                display_xp(Player1)
            else:
                print("No valid save data found.\n")
        elif option == 'n':
            print("\n----- Creating New Save -------")
        else:
            print("Invalid choice. Please enter 'y' or 'n'.\n")
    else:
        print("Player data already loaded.\n")


    if not Player1:
        print("It seems like you don't have a character saved yet. Let's create one!")
        reset_data() 
        Player1 = Player_entity()  
        print_player_data(Player1)  
        display_xp(Player1)
        first_save(Player1)  
    player_name = Player1.get("Player", {}).get("name", "Unknown Player")
    # skill_points = Player1.get("Player", {}).get("Current Level", {}).get("Skill Points", 0)
    
    print(f"\n---- Welcome back, {player_name} ----")
    
    xp_manager = ExperienceManager(Player1)
    print("Here, have some experience points!")
    xp_manager.gain_xp(3) 

    save_data(Player1)

if __name__ == "__main__":
    main()
