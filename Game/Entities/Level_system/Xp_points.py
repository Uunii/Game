import json


# XP does not roll over for the next level currently (resets to 0 upon level up)
 
class ExperienceManager:
    filename = "Game/Entities/SaveData/Player.json"

    def __init__(self, player_data):
        self.data = player_data 
        self.level = self.data.get("Current Level", 0)
        self.xp = self.data["xp"].get("Experience (xp)", 0)
        self.xp_needed = self.data["xp"].get("Xp needed to level up", 10)
        
    
    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=2)

    def gain_xp(self, amount):
        self.data["xp"]["Experience (xp)"] += amount
        self.xp = self.data["xp"]["Experience (xp)"]  
        print(f"Gained {amount} XP! Total XP: {self.xp}/{self.xp_needed}")

        if self.xp >= self.xp_needed:
            self.level_up()

        self.save_data()  

    def level_up(self):
        self.data["Current Level"] += 1
        self.data["xp"]["Experience (xp)"] = 0  
        self.data["xp"]["Xp needed to level up"] = int(self.xp_needed * 1.2)  

        self.level = self.data["Current Level"]
        self.xp_needed = self.data["xp"]["Xp needed to level up"]

        print(f"\n=============== Alert ============= \n🎉 You Leveled Up to level {self.level} 🎉\n XP needed for next level: 0/{self.xp_needed}xp")

        self.save_data()  

    
