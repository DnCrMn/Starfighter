# Class that represents an enemy. Child class of entity 
from entities.entity import Entity

class Enemy(Entity):
    def __init__(self, name, health, attack, defense, fleeChance = 100, ascii = None):
        super().__init__(name, health, attack, defense)
        self.fleeChance = fleeChance
        self.ascii = ascii or []

    # Type should be enemy
    def getType(self):
        return "Enemy"
