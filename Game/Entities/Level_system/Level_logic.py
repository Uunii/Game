import json



class Level():
    def __init__(self, level):
        self.level = level

    def get_level(self):
        try: 
            with open("Game/Entities/SaveData/Player.json", "r") as f:
                data = json.load(f)
            current_level = data.get("Current Level", "Key not found")
            return current_level
        except json.decoder.JSONDecodeError as e:
            print("Creating new character")
            return 0
    def level_up(self):
        with open("Game/Entities/SaveData/Player.json", "r") as f:
            data = json.load(f)
        current_level = data.get("Current Level", "Key not found")
        current_level += 1
        data["Current Level"] = current_level
        with open("Game/Entities/SaveData/Player.json", "w") as f:
            json.dump(data, f, indent=2)
        print(f"{self.level} : current_level")
    def reset_level(self):
        with open("Game/Entities/SaveData/Player.json", "r") as f:
            data = json.load(f)
        current_level = data.get("Current Level", "Key not found")
        current_level = 0
        data["Current Level"] = current_level
        with open("Game/Entities/SaveData/Player.json", "w") as f:
            json.dump(data, f, indent=2)