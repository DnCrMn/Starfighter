# Script that handles enemy encounters
import json
import random
from utilities.utils import getIntChoice, slowPrint, slowInput
from systems.combat import engageCombat
from entities.ship import Ship
from entities.enemy import Enemy

# Load Necessary data 
with open("data/ships.json") as shipFile:
    shipsData = json.load(shipFile)

with open("data/items.json") as itemFile:
    itemsData = json.load(itemFile)["items"] # Get value inside "items" key

with open("data/encounters.json") as encountersFile:
    encountersData = json.load(encountersFile)["encounters"] # Get value inside "encounters" key

# Chooses the player's ship
def chooseShip():
    slowPrint("\nChoose your ship:")

    # Print the availabe ships
    for index, shipName in enumerate(shipsData, start = 1):
        data = shipsData[shipName]
        slowPrint(f"{index}) {shipName} - Health: {data['health']} | ATK: {data['attack']} | DEF: {data['defense']}", 0.05)

    shipNames = list(shipsData.keys()) # Get list of ship names

    # Loop until player choose a valid input
    choice = getIntChoice("\nEnter the ship's number:\n> ", 1, len(shipNames))

    # Get ship that the player has chosen
    chosenShip = shipNames[choice - 1]
    data = shipsData[chosenShip]

    return Ship(chosenShip, data["health"], data["attack"], data["defense"])

# Gets a random enemy encounter
# Final is true if encounter is boss
def getRandomEncounter(final = False):
    if final:
        return next(encounter for encounter in encountersData if encounter.get("final"))
    return random.choice([encounter for encounter in encountersData if not encounter.get("final")])

# Returns an enemy depending on the encounter
def createEnemyFromEncounter(encounter):
    return Enemy(
        name = encounter["name"],
        health = encounter["health"],
        attack = encounter["attack"],
        defense = encounter["defense"],
        fleeChance = encounter["flee_chance"],
        ascii = encounter["ascii"]
    )


# Triggers random encounter
def triggerRandomEncounter(player, final = False):
    encounter = getRandomEncounter(final)

    # If encounter type is combat, engage with them
    if encounter["type"] == "combat":
        enemy = createEnemyFromEncounter(encounter)
        survived = engageCombat(player, enemy)
        return survived
    elif encounter["type"] == "item":
        slowPrint(f"\nYou enter a/an {encounter['name']}...")

        # Randomize item pick-up
        itemName = random.choice(encounter["items"])
        item = next(i for i in itemsData if i["name"] == itemName)
        player.addItem(item)

        return True
