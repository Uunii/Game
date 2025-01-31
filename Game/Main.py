from Entities.Player_entity import Player_entity
from Entities.Enemy_entity import Enemy_entity
from Entities.Level_system.Level_logic import Level
from Entities.Level_system.Xp_points import ExperienceManager  
import json

filename = "Game/Entities/SaveData/Player.json"

Player1 = {}

# 
def update_data():
    try:
        with open(filename, 'r') as f:
            data = json.load(f)
        return data
    except (json.decoder.JSONDecodeError, FileNotFoundError):
        return {}


def save_data(data):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2)

def reset_data():
    with open("Game/Entities/SaveData/Player.json", 'w') as f:
        f.write("")
        
def first_save(data):
    save_data(data)

def Save_level():
    player_level = Level()
    player_level.level_up()
    Player1["Current Level"] = player_level.get_level()
    save_data(Player1)

def Reset_level():
    player_level = Level()
    player_level.reset_level()
    Player1["Current Level"] = player_level.get_level()
    save_data(Player1)

def display_xp(player):
    xp_info = player.get("xp", {})
    if xp_info:
        print("🎮 XP Status 🎮")
        print(f"🔹 XP: {xp_info.get('Experience (xp)', 0)}/{xp_info.get('Xp needed to level up', 0)}")
        print("-" * 30)


def main():
    global Player1  
    print(" --- Welcome to the game! ---")
    
    if not Player1:
        print("Would you like to load from a previous save?\n")
        option = input("Enter choice (y/n): ")
        if option.lower() == 'y':
            previous_save = update_data()
            Player1.update(previous_save)
            print("\n------ Current Save ----------")
            
            for key, val in Player1.items():
                if key != "xp":
                    print(f"{key} : {val}")
            
            if "xp" in Player1:
                display_xp(Player1)
                
        elif option.lower() == 'n':
            print("\n----- Creating New Save -------")
        else:
            print("No SaveData found")

    while not Player1:
        reset_data()
        Player1.update(Player_entity()) 
        print("\nYour Character:")
        for key, val in Player1.items():
            if key != "xp":
                print(f"{key} : {val}")
        display_xp(Player1)
        first_save(Player1)

    print(f"\n ---- Welcome back, {Player1['name']} ----")
    

    xp_manager = ExperienceManager(Player1)  

    print("Here, have some experience points!")
    xp_manager.gain_xp(22)  

    save_data(Player1)
    


if __name__ == "__main__":
    app = main()