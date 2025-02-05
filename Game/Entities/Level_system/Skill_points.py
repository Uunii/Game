import json
import os

class SkillPoints:

    filename = "Game/Entities/SaveData/Player.json"

    def __init__(self, player_data=None):
        if player_data is None:
            self.data = self.load_data()
        else:
            self.data = player_data

        if not isinstance(self.data.get("Current Level"), dict):
            self.data["Current Level"] = {"Level": 0, "Skill Points": 0}

        self.level_info = self.data["Current Level"]
        self.level_info.setdefault("Skill Points", 0)

    def load_data(self):
        try:
    
            if not os.path.exists(self.filename):
                print(f"{self.filename} not found, creating new character data.")
                return {"Current Level": {"Level": 0, "Skill Points": 0}}

            with open(self.filename, "r") as f:
                return json.load(f)
            
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading player data: {e}")
            return {"Current Level": {"Level": 0, "Skill Points": 0}}

    def save_data(self):
        try:
            with open(self.filename, "w") as f:
                json.dump(self.data, f, indent=2)
            print("Player data saved successfully.")

        except Exception as e:
            print(f"Error saving player data: {e}")

    def get_SP(self):
        skill_points = self.data.get("Current Level", {}).get("Skill Points", 0)
        print(f"Total Skill Points: {skill_points}")

        max_sp = 50
        if skill_points > max_sp:
            print(f"Warning: Skill points have exceeded the maximum limit of {max_sp}. Resetting to {max_sp}.")
            skill_points = max_sp  # Reset skill points to max_sp if exceeded
            self.level_info["Current Level"]["Skill Points"] = skill_points

        if skill_points > 10:
            print(f"+ You should consider using your {skill_points} Skill Points!")
        else:
            print("Use your skill points wisely!")

        self.save_data()
