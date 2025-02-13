from colorama import init, Fore, Back, Style

def Sorcerer():
    print(Fore.BLUE,Style.BRIGHT,'\n            .')
    print(f'           /:\ ')
    print(f'          /;:.\ ')
    print(f'         //;:. \ ')
    print(f'        ///;:.. \ ')
    print(f'  __--"////;:... \ "-__')
    print(f'--__   "--_____--"   __--')
    print(f'    """--_______--"""    \n',Fore.WHITE)
def Knight():
    print(Fore.YELLOW,Style.BRIGHT,"\n  |`-._/\_.-`|")
    print(f"  |    ||    |")
    print(f"  |___o()o___|")
    print(f"  |__{Fore.RED}((<>)){Fore.YELLOW}__|")
    print(f"  \   o\/o   /")
    print(f"   \   ||   /")
    print(f"    \  ||  /")
    print(f"     '.||.'",Fore.WHITE,Style.NORMAL)
def Marksman():
    print(f"                    {Fore.RED}⢀⣤⡾⠉⣹⠇⠀")
    print(f"        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡟⢁⣼⣿⠏⠀⠀⠀")
    print(f"{Fore.GREEN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣦{Fore.RED}⠀⢀⣾⡟⢠⣾⣿⠃⠀⠀⠀⠀")
    print(f"{Fore.GREEN}⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡇{Fore.RED}⣼⡟⢠⣿⡿⠁⠀⠀⠀⠀⠀")
    print(f"{Fore.GREEN}⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⡇{Fore.RED}⡟⢀⣾⠟⠀⠀⠀⠀⠀⠀⠀")
    print(f"{Fore.GREEN}⠀⠀⠀⢀⣴⠞⢁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⢈⣠⠀⠀⠀⠀⠀⠀⠀⠀")
    print(f"⠀⠀⣰⡿⠁⣴⣿⣿⣿⣿⣿⣿⠿⠟⠋⣉⣠⣴⠾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀")
    print(f"⠀⢰⠏⣠⣾⣿⣿⠿⠛⠋⣉⣠⣴⣶⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
    print(f"⠀⠁⠞⠛⠉⡁⠤⠴⠞⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n")
def Title():
    print("\n\n")
    print(Fore.GREEN,Style.BRIGHT,f"   __     __  __     __   __     ______     __         ______ ")         
    print("    /\ \   /\ \/\ \   /\  -.\ \   /\  ___\   /\ \       /\  ___\ ")           
    print("   _ _\ \  \ \ \_\ \  \ \ \-.  \  \ \ \__ \  \ \ \____  \ \  __\ ")         
    print("  /\_____\  \ \_____\  \ \_\\  \ \  \ \_____\  \ \_____\  \ \_____\ ")        
    print("  \/_____/   \/_____/   \/_/ \/_/   \/_____/   \/_____/   \/_____/")                                                                              
    print("   ______     ______      _____     ______     __  __     __     _____ ")   
    print("  /\  __ \   /\  ___\    /\  __-.  /\  == \   /\ \/\ \   /\ \   /\  __ \ ") 
    print("  \ \ \/\ \  \ \  __\    \ \ \/\ \ \ \  __<   \ \ \_\ \  \ \ \  \ \ \/\ \ ") 
    print("   \ \_____\  \ \_\       \ \____-  \ \_\ \_\  \ \_____\  \ \_\  \ \____/ ") 
    print("    \/_____/   \/_/        \/____/   \/_/ /_/   \/_____/   \/_/   \/____/\n",Fore.WHITE,Style.NORMAL) 

def showClasses():
        print(Fore.BLUE + Style.BRIGHT + '\n\n            .' + " " * 15 + Fore.YELLOW + Style.BRIGHT + "  |`-._/\_.-`|" + " " * 10 + Fore.YELLOW + "⠀⠀⠀⠀⠀⠀⠈⣿.⡀⠀⠀⠀⠀" + " " * 10 + Fore.RED + "                    ⢀⣤⡾⠉⣹⠇⠀")
        print(Fore.BLUE + '           /:\ ' + " " * 13 + Fore.YELLOW + "  |    ||    |" + " " * 10 + Fore.YELLOW + "⠀⠀⠀ ⠀⡀⢠⣿⡟⣿⣿⠀⠀" + " " * 11 + Fore.RED + "        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⡟⢁⣼⣿⠏⠀⠀⠀")
        print(Fore.BLUE + '          /;:.\ ' + " " * 12 + Fore.YELLOW + "  |___o()o___|" + " " * 10 + Fore.YELLOW + "⠀⠀ ⠀⠀⣳⣼⣿⡏⢸⣿⣿⢀⠀" + " " * 10 + Fore.GREEN + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⣾⣦" + Fore.RED + "⠀⢀⣾⡟⢠⣾⣿⠃⠀⠀⠀⠀")
        print(Fore.BLUE + '         //;:. \ ' + " " * 11 + Fore.YELLOW + "  |__" + Fore.RED + "((<>))" + Fore.YELLOW + "__|" + " " * 10 + Fore.YELLOW + "⠀ ⠀⠀⣰⣿⣿⡿⠁⢸⣿⣿⡟⣼" + " " * 10 + Fore.GREEN + "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⡇" + Fore.RED + "⣼⡟⢠⣿⡿⠁⠀⠀⠀⠀⠀")
        print(Fore.BLUE + '        ///;:.. \ ' + " " * 10 + Fore.YELLOW + "  \   o\/o   /" + " " * 10 + Fore.YELLOW + " ⢰⢀⣾⣿⣿⠟⠀⠀⣾⢿⣿⣿⣿" + " " * 10 + Fore.GREEN + "⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⡇" + Fore.RED + "⡟⢀⣾⠟⠀⠀⠀⠀⠀⠀⠀")
        print(Fore.BLUE + '  __--"////;:... \ "-__' + " " * 5 + Fore.YELLOW + "   \   ||   /" + " " * 11 + Fore.YELLOW + " ⢸⣿⣿⣿⡏⠀⠀⠀⠃⠸⣿⣿⣿" + " " * 10 + Fore.GREEN + "⠀⠀⠀⢀⣴⠞⢁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⢈⣠⠀⠀⠀⠀⠀⠀⠀⠀")
        print(Fore.BLUE + '--__   "--_____--"   __--' + " " * 3 + Fore.YELLOW + "    \  ||  /" + " " * 13 + Fore.RED + "⢳⣿⣿⣿" + " " * 2 + Fore.CYAN + "⣿⣿" + " " * 2 + Fore.RED + "⢹⣿⡁" + " " * 10 + Fore.GREEN + "⠀⠀⣰⡿⠁⣴⣿⣿⣿⣿⣿⣿⠿⠟⠋⣉⣠⣴⠾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀")
        print(Fore.BLUE + '    """--_______--"""' + " " * 7 + Fore.YELLOW + "     '.||.'" + Fore.WHITE + Style.NORMAL + " " * 13 + Fore.YELLOW + "⠀ ⠹⣿⣿⡄ ⡄ ⡄⢠⣿⡞⠁" + " " * 10 + Fore.GREEN + "⠀⢰⠏⣠⣾⣿⣿⠿⠛⠋⣉⣠⣴⣶⠿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print(" " * 76 + Fore.GREEN + "⠀⠁⠞⠛⠉⡁⠤⠴⠞⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n",Fore.WHITE)
        print("     1 - Sorcerer             2 - Knight            3 - Pyromancer              4 - Marksman\n")

Title()
showClasses()