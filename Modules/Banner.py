from colorama import Fore, Style

BANNER = """                          
           /(((((((*          
       ((((((((#########      
          ((((((((((((((((     _____                    __                                
   ######## (((((             |_   _|                  / _|                              
   ### (((((((((/ ##########    | | ___ _ __ _ __ __ _| |_ ___  _ __ _ __ ___   ___ _ __ 
  ####       (((((((((( #####   | |/ _ | '__| '__/ _` |  _/ _ \| '__| '_ ` _ \ / _ | '__|
   ########### (((((   #####    | |  __| |  | | | (_| | || (_) | |  | | | | | |  __| |   
   (((((((((((((((( ########    \_/\___|_|  |_|  \__,_|_| \___/|_|  |_| |_| |_|\___|_| 
     (((((  #####  (((((((    
       ((( ####### (((((      
           .((((((( """


def printBanner():
    print(Fore.LIGHTBLUE_EX + "           /(((((((*")
    print(Fore.LIGHTBLUE_EX + "       ((((((((" + Fore.GREEN + "#########")
    print(Fore.LIGHTBLUE_EX + "          ((((((((((((((((" + Fore.CYAN + "     _____")
    print(
        Fore.GREEN + "   ########" + Fore.LIGHTBLUE_EX + " ((((( " + Fore.CYAN + "            |_   _|                  / _|")
    print(
        Fore.GREEN + "   ###" + Fore.LIGHTBLUE_EX + " (((((((((/" + Fore.GREEN + " ##########  " + Fore.CYAN + "  | | ___ _ __ _ __ __ _| |_ ___  _ __ _ __ ___   ___ _ __ ")
    print(
        Fore.GREEN + "  ####" + Fore.LIGHTBLUE_EX + "       (((((((((( " + Fore.GREEN + "#####  " + Fore.CYAN + " | |/ _ | '__| '__/ _` |  _/ _ \| '__| '_ ` _ \ / _ | '__|")
    print(
        Fore.GREEN + "   ###########" + Fore.LIGHTBLUE_EX + " ((((( " + Fore.GREEN + "  ##### " + Fore.CYAN + "   | |  __| |  | | | (_| | || (_) | |  | | | | | |  __| |   ")
    print(
        Fore.LIGHTBLUE_EX + "   ((((((((((((((((" + Fore.GREEN + " ######## " + Fore.CYAN + "   \_/\___|_|  |_|  \__,_|_| \___/|_|  |_| |_| |_|\___|_| ")
    print(Fore.LIGHTBLUE_EX + "     ((((( " + Fore.GREEN + " ##### " + Fore.LIGHTBLUE_EX + " (((((((")
    print(Fore.LIGHTBLUE_EX + "       ((( " + Fore.GREEN + "#######" + Fore.LIGHTBLUE_EX + " (((((")
    print(Fore.LIGHTBLUE_EX + "           .((((((( " + Style.RESET_ALL)
