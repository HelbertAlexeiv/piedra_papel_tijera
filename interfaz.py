from colorama import Fore, Style
from os import system
class main():
    def __init__(self) -> None:
        self.rock = """
  _____    _____   ______   _____    _____             
 |  __ \  |_   _| |  ____| |  __ \  |  __ \      /\    
 | |__) |   | |   | |__    | |  | | | |__) |    /  \   
 |  ___/    | |   |  __|   | |  | | |  _  /    / /\ \  
 | |       _| |_  | |____  | |__| | | | \ \   / ____ \ 
 |_|      |_____| |______| |_____/  |_|  \_\ /_/    \_\
                """
        self.paper = """
  _____               _____    ______   _      
 |  __ \      /\     |  __ \  |  ____| | |     
 | |__) |    /  \    | |__) | | |__    | |     
 |  ___/    / /\ \   |  ___/  |  __|   | |     
 | |       / ____ \  | |      | |____  | |____ 
 |_|      /_/    \_\ |_|      |______| |______|
                """

        self.sisors = """
  _______   _____        _   ______   _____                _____ 
 |__   __| |_   _|      | | |  ____| |  __ \      /\      / ____|
    | |      | |        | | | |__    | |__) |    /  \    | (___  
    | |      | |    _   | | |  __|   |  _  /    / /\ \    \___ \ 
    | |     _| |_  | |__| | | |____  | | \ \   / ____ \   ____) |
    |_|    |_____|  \____/  |______| |_|  \_\ /_/    \_\ |_____/ 
                 """   

        self.choose = ["1)Piedra", "2)Papel", "3)Tijera"]
        self.words = [self.rock, self.paper, self.sisors]
        self.opcions = ["                 1) iniciar", "                 2) salir"]
        self.colors = [Fore.BLUE, Fore.WHITE, Fore.RED, Fore.GREEN]

    def main_print(self, index):
        return self.words[index]

    def main_opcions(self, index):
        return self.opcions[index] 

    def choose_rock_paper_scissors(self):
        count = 0
        for i in self.choose:
            print(self.colors[count],self.choose[count])
            count += 1
            print(Style.RESET_ALL)

    def welcome(self):
        count = 0
        opcion = str()
        for i in range(3):
            print(self.colors[count],self.main_print(count))
            count += 1
        count = 0
        for i in range(2):
            print(self.colors[3], self.main_opcions(count))
            count += 1
        opcion = input("Ingrese una opcion: ")
        if opcion == "2":
            system("clear")
            exit()
        else:
            system("clear")

        def colors_list(self):
            return self.colors




