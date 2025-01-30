from abc import ABC, abstractmethod

# Race Selector for player 
Race_selected = {}

class Races(ABC):

    racelist = ["Demon", "Angel", "Human", "Beast", "Mix", "Elf", "Lost Soul"]
    def __init__(self, name, race, affinity):
        self.name = name
        self.race_type = race  
        self.affinity = affinity

    @abstractmethod
    def race(self):
        pass 

# Races: Demon, angel, human, beast, mix, elf, lost soul
class Demon(Races):
    def __init__(self, name):
        super().__init__(name, "Demon", "Evil")
    def race(self):
        return self.race_type
    def affinity(self):
        return self.affinity
    def demon_attributes(self):
        print(f"Some attribute {self.affinity}")

class Angel(Races):
    def __init__(self, name):
        super().__init__(name, "Angel", "Pure")
    def race(self):
        return self.race_type
    def affinity(self):
        return self.affinity
    def Angel_attributes(self):
        print(f"Some attribute {self.affinity}")

class Human(Races):
    def __init__(self, name):
        super().__init__(name, "Human", "Neutral")
    def race(self):
        return self.race_type
    def affinity(self):
        return self.affinity
    def Human_attributes(self):
        print(f"Some attribute {self.affinity}")

class Beast(Races):
    def __init__(self, name):
        super().__init__(name, "Beast", "Neutral")
    def race(self):
        return self.race_type
    def Beast_attributes(self):
        print(f"Some attribute: {self.affinity}")


class Elf(Races):
    def __init__(self, name):
        super().__init__(name, "Elf", "Pacifist")
    def race(self):
        return self.race_type
    def affinity(self):
        return self.affinity
    def Elf_attributes(self):
        print(f"Some attribute: {self.afiinity}")


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
                Race_selected.update({
                    "Race": chosen_race,
                    "Affinity": character.affinity
                })
            print(f"\nRace Status:")
            for key, val in Race_selected.items():
                print(f"{key} : {val}")
        else:
            print("Invalid choice. Please select a valid number.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    return chosen_race



