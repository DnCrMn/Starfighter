# Class that holds the player data
from systems.item_effects import itemEffects
from utilities.utils import slowPrint, slowInput

class Player:
    def __init__(self, name):
        self.name = name
        self.ship = None
        self.inventory = []

    # Sets the ship that the player will be using
    def setShip(self, ship):
        self.ship = ship

    # Adds item to the inventory
    def addItem(self, item):
        self.inventory.append(item)
        slowPrint(f"You have acquired: {item["name"]}!")
        slowInput("\n[Press ENTER to continue]")

    # Uses the in your inventory given its name.
    # Returns true if item use is successful
    def useItem(self, itemName):
        # Return immediately if there are no items in the inventory
        if not self.inventory: 
            return False 

        for item in self.inventory:
            # Make sure string comparisons are both lower case 
            if item["name"].lower() == itemName["name"].lower():
                effect = itemEffects.get(item["type"]) # Get effect from item type

                # if effect is not empty, apply to player
                if effect:
                    effect(self, item["value"])
                    self.inventory.remove(item)
                    return True # Do not loop further; Only use this item.
                else:
                    slowPrint("No effect found for this item.")
                    return False
        slowPrint("Item not found in inventory.")
        return false

    # Decreases ships health
    def takeDamage(self, damage):
        return self.ship.takeDamage(damage)

    # Checks if the player is alive
    def isAlive(self):
        return self.ship.isAlive()
