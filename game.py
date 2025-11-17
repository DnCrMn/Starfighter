# Class that handles the main game loop for the text adventure.
from entities.player import Player
from systems.encounters import chooseShip
from scenes.scene_runner import runPath
from utilities.utils import slowPrint, slowInput, printASCII

def start():
    # Header for the game
    slowPrint("""
           ,-,--.  ,--.--------.   ,---.                      _,---.   .=-.-.
         ,-.'-  _\\/==/,  -   , -\\.--.'  \\      .-.,.---.   .-`.' ,  \\ /==/_ /
        /==/_ ,_.'\\==\\.-.  - ,-./\\==\\-/\\ \\    /==/  `   \\ /==/_  _.-'|==|, | 
        \\==\\  \\    `--`\\==\\- \\   /==/-|_\\ |  |==|-, .=., /==/-  '..-.|==|  | 
         \\==\\ -\\        \\==\\_ \\  \\==\\,   - \\ |==|   '='  /==|_ ,    /|==|- | 
         _\\==\\ ,\\       |==|- |  /==/ -   ,| |==|- ,   .'|==|   .--' |==| ,| 
        /==/\\/ _ |      |==|, | /==/-  /\\ - \\|==|_  . ,'.|==|-  |    |==|- | 
        \\==\\ - , /      /==/ -/ \\==\\ _.\\=\\.-'/==/  /\\ ,  )==/   \\    /==/. / 
         `--`---'       `--`--`  `--`        `--`-`--`--'`--`---'    `--`-`  
              _,---.  ,--.-,,-,--,,--.--------.    ,----.                    
          _.='.'-,  \\/==/  /|=|  /==/,  -   , -\\,-.--` , \\  .-.,.---.        
         /==.'-     /|==|_ ||=|, \\==\\.-.  - ,-./==|-  _.-` /==/  `   \\       
        /==/ -   .-' |==| ,|/=| _|`--`\\==\\- \\  |==|   `.-.|==|-, .=., |      
        |==|_   /_,-.|==|- `-' _ |     \\==\\_ \\/==/_ ,    /|==|   '='  /      
        |==|  , \\_.' )==|  _     |     |==|- ||==|    .-' |==|- ,   .'       
        \\==\\-  ,    (|==|   .-. ,\\     |==|, ||==|_  ,`-._|==|_  . ,'.       
         /==/ _  ,  //==/, //=/  |     /==/ -//==/ ,     //==/  /\\ ,  )      
         `--`------' `--`-' `-`--`     `--`--``--`-----`` `--`-`--`--'       
    """, 0.005)

    # Choose player name and ship
    name = slowInput("\nWhat is your name, soldier? ")
    player = Player(name)
    player.setShip(chooseShip())
    slowPrint(f"\nWelcome aboard, Cadet Lieutenant {player.name}. You are currently flying the {player.ship.name}!")

    # Trigger random encounters + 1 boss
    runPath(player)

    slowPrint(f"\nCadet Lieutenant {player.name}, your adventure ends here.")
    slowPrint(f"Final ship status: {player.ship}")

    # Convert inventory into a comma-separated string
    inventoryString = ", ".join(item["name"] for item in player.inventory)
    slowPrint(f"Inventory collected: {inventoryString}")
