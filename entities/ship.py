# Class that holds the ship data. Child class of entity
from entities.entity import Entity

class Ship(Entity):
    def __init__(self, name, health, attack, defense):
        super().__init__(name, health, attack, defense)
    
    # Type should be player
    def getType(self):
        return "Player"
