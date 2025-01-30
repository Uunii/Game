
# Menu items and choice option logic

class MenuHandler:
    def __init__(self, menu):
        self.menu = menu

    def menu_items(self, character_type=None):
        menus = {
            "Start": ["Start Menu", "1 - Create Character", "2 - Simulate Battle", "3 - Exit"],
            "Game": ["\nCurrent Moves", "1 - Attack", "2 - Defend", "3 - Exit"],
            "Error": ["\nError Encountered", "Exiting Battle..", "Try again"],
            "Characters": ["\nSelect Character Type", "1 - Wizard", "2 - Warrior", "3 - Archer"],
            "Wizard Weapon": ["\nSelect Wizard Weapon", "1 - Wand", "2 - Dual Wand"],
            "Warrior Weapon": ["\nSelect Warrior Weapon", "1 - Sword", "2 - Dual Sword"],
            "Wizard Defense": ["\nSelect Wizard Defense", "1 - Magic Barrier", "2 - None"],
            "Warrior Defense": ["\nSelect Warrior Defense", "1 - Shield", "2 - None"],
            "Archer Weapon": ["\nSelect Arrow type", "1 - Fire arrow", "2 - Silver Arrow"],
            "Archer Defense": ["\nSelect Archer Defense", "1 - Dagger throw", "2 - Run"],
        }
        
        if character_type == "Wizard":
            return menus.get("Wizard Weapon", ["Invalid Menu"])
        elif character_type == "Warrior":
            return menus.get("Warrior Weapon", ["Invalid Menu"])
        elif character_type == "Arhcer":
            return menus.get("Archer Weapon", ["Invalid Menu"])

        return menus.get(self.menu, ["Invalid Menu"])

    def format_menu(self, character_type=None):
        items = self.menu_items(character_type)
        for item in items:
            print(item)

    @staticmethod
    def choice():
        tries = 0
        while tries < 3:
            try:
                choice = int(input("Enter choice (1-3): "))
                if 1 <= choice <= 3:
                    return choice
                print(f"\nInvalid choice. Try again ({2 - tries} attempts left)")
                tries += 1
            except ValueError:
                print(f"\nInvalid input. Try again ({2 - tries} attempts left)")
                tries += 1
        print("Too many invalid attempts. Exiting...")
        exit()