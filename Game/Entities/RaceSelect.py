from abc import ABC, abstractmethod
import json


Race_selected = {}

class Races(ABC):
    filename = "Game/Entities/SaveData/Player.json"
    racelist = ["Demon", "Angel", "Human", "Beast", "Mix", "Elf", "Lost Soul"]

    def __init__(self, name, race, affinity, skill):
        self.name = name
        self.race_type = race  
        self.affinity = affinity
        self.unique_skill = skill
        self.data = {}  

    @abstractmethod
    def race(self):
        pass 

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump(self.data, f, indent=2)


class Demon(Races):
    def __init__(self, name):
        super().__init__(name, "Demon", "Evil", "Faint deception")

    def race(self):
        return self.race_type

    def affinity(self):
        return self.affinity

    def demon_attributes(self):
        print(f"Some attribute {self.affinity}")


class Angel(Races):
    def __init__(self, name):
        super().__init__(name, "Angel", "Pure", "Golden Era")

    def race(self):
        return self.race_type

    def affinity(self):
        return self.affinity

    def Angel_attributes(self):
        print(f"Some attribute {self.affinity}")

class Human(Races):
    def __init__(self, name):
        super().__init__(name, "Human", "Neutral", "Determination")

    def race(self):
        return self.race_type

    def affinity(self):
        return self.affinity

    def Human_attributes(self):
        print(f"Some attribute {self.affinity}")

class Beast(Races):
    def __init__(self, name):
        super().__init__(name, "Beast", "Neutral", "Ravage")

    def race(self):
        return self.race_type

    def affinity(self):
        return self.affinity

    def Beast_attributes(self):
        print(f"Some attribute: {self.affinity}")

class Elf(Races):
    def __init__(self, name):
        super().__init__(name, "Elf", "Pacifist", "Silent Hero")

    def race(self):
        return self.race_type

    def affinity(self):
        return self.affinity

    def Elf_attributes(self):
        print(f"Some attribute: {self.affinity}")


raceDictionary = {
    "Demon": Demon,
    "Angel": Angel,
    "Human": Human,
    "Beast": Beast,
    "Elf": Elf
}

def RaceSelector():
    
    print("---- Race Selector ----")
    for i, race in enumerate(Races.racelist, start=1):
        print(f"{i}. {race}")

    try:
        option = int(input("Enter the number of your chosen race: "))
        if 1 <= option <= len(Races.racelist):
            chosen_race = Races.racelist[option - 1]

            if chosen_race in raceDictionary:
                character = raceDictionary[chosen_race]("Player")

                return {
                    "Name": character.race_type,
                    "affinity": character.affinity,  
                    "unique skill": character.unique_skill
                }
        else:
            print("Invalid choice. Please select a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return None