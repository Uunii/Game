import json
import os

class Level():
    def __init__(self):
        self.level = self.get_level()
        #self.xp_needed = self.get_xp_for_next_level()  

    def get_level(self):
        try:
            if not os.path.exists("Game/Entities/SaveData/Player.json"):
                print("Save file not found, creating new character.")
                return 0

            with open("Game/Entities/SaveData/Player.json", "r") as f:
                data = json.load(f)
        
            current_level = data.get("Player", {}).get("Current Level", {}).get("Level", 0)
            return current_level

        except json.decoder.JSONDecodeError as e:
            return 0
        except Exception as e:
            print(f"An error occurred: {e}")
            return 0

    def reset_level(self):
     
        self.level = 0
        self.xp_needed = self.get_xp_for_next_level() 

        try:
            with open("Game/Entities/SaveData/Player.json", "r") as f:
                data = json.load(f)

            if "Player" not in data:
                data["Player"] = {}

            if "Current Level" not in data["Player"]:
                data["Player"]["Current Level"] = {}

            data["Player"]["Current Level"]["Level"] = self.level  
            data["Player"]["Current Level"]["Xp Needed for Next Level"] = self.xp_needed
            
            if "Current Level" in data:
                del data["Current Level"]

            with open("Game/Entities/SaveData/Player.json", "w") as f:
                json.dump(data, f, indent=2)

            print(f"Level reset to {self.level}")

        except Exception as e:
            print(f"An error occurred while resetting the level: {e}")
