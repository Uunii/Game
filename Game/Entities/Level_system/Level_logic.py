import json

class Level():
    def __init__(self):
        self.level = self.get_level()  

    def get_level(self):
        try: 
           
            with open("Game/Entities/SaveData/Player.json", "r") as f:
                data = json.load(f)
            current_level = data.get("Current Level", 0)  
            return current_level
        except json.decoder.JSONDecodeError as e:
            print("Error loading the file, creating new character.")
            return 0 

    def level_up(self):
        self.level += 1
        with open("Game/Entities/SaveData/Player.json", "r") as f:
            data = json.load(f)  
        data["Current Level"] = self.level
        with open("Game/Entities/SaveData/Player.json", "w") as f:
            json.dump(data, f, indent=2)  
        print(f"You have Leveled up to Level: {self.level}!")  


    def reset_level(self):
        self.level = 0
        with open("Game/Entities/SaveData/Player.json", "r") as f:
            data = json.load(f)
        data["Current Level"] = self.level  
        with open("Game/Entities/SaveData/Player.json", "w") as f:
            json.dump(data, f, indent=2)
        print(f"Level reset to {self.level}")

