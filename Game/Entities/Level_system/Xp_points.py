import json

class ExperienceManager:

    filename = "Game/Entities/SaveData/Player.json"

    def __init__(self, player_data=None):
        if player_data is None:
            self.data = self.load_data()
        else:
            self.data = player_data
        if "Player" not in self.data:
            self.data["Player"] = {}

        player_data = self.data["Player"]
        if "Current Level" not in player_data:
            player_data["Current Level"] = {"Level": 0, "Skill Points": 0}

        self.level_info = player_data["Current Level"]
        self.level = self.level_info.get("Level", 0)

        if not isinstance(self.level, int):
            print(f"Warning: 'Level' is not an integer. Setting it to 0.")
            self.level_info["Level"] = 0  

        if "xp" not in player_data:
            player_data["xp"] = {"Experience (xp)": 0, "Xp needed to level up": 10}

        self.xp = player_data["xp"].get("Experience (xp)", 0)
        self.xp_needed = self.get_xp_for_next_level() 

    def load_data(self):
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}. Initializing new player data.")
            return {"Player": {"Current Level": {"Level": 0, "Skill Points": 0}, "xp": {"Experience (xp)": 0, "Xp needed to level up": 10}}}

    def save_data(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.data, f, indent=2)
        except Exception as e:
            print(f"Error saving data: {e}")

    def get_xp_for_next_level(self):
        base_xp = 10  
        scaling_factor = 1.2  
        xp_for_next_level = int(base_xp * (scaling_factor ** self.level))
        return xp_for_next_level

    def gain_xp(self, amount):
        if amount < 0 and self.xp + amount < 0:
            print("XP cannot go below 0!")
            return  
        
        self.xp += amount
        self.data["Player"]["xp"]["Experience (xp)"] = self.xp  

        if amount > 0:
            print(f"+ Gained {amount} XP\nTotal XP: {self.xp}/{self.xp_needed} XP")
        else:
            print(f"- Lost {abs(amount)} XP\nTotal XP: {self.xp}/{self.xp_needed} XP")

        while self.xp >= self.xp_needed:
            self.xp -= self.xp_needed  
            self.level_up()

        self.data["Player"]["xp"]["Experience (xp)"] = self.xp
        self.save_data()

    def level_up(self):
        self.level_info["Level"] += 1
        self.level_info["Skill Points"] += 5
        self.xp_needed = self.xp_needed + 5  # 
        self.data["Player"]["xp"]["Xp needed to level up"] = self.xp_needed
        print(f"🎉 Level Up! You are now Level {self.level_info['Level']}")
        print(f"🎯 You gained 5 Skill Points! Total SP: {self.level_info['Skill Points']}")
        print(f"🆙 Next Level XP Required: {self.xp_needed} XP")
