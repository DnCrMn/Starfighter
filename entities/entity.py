# Abstract class that represents an entity inside of the game
from abc import ABC, abstractmethod
from typing import override

class Entity(ABC):
    def __init__(self, name, maxHealth, attack, defense):
        self.name = name
        self.health = maxHealth
        self.maxHealth = maxHealth
        self.attack = attack
        self.defense = defense
    
    # Checks if the entity is alive
    def isAlive(self):
        return self.health > 0
    
    # Function for decreasing entity health based on attacker's damage and 
    # Entity's defense
    def takeDamage(self, damage):
        # Calculate damage mitigation based on defense
        finalDamage = round((100 * damage)/(self.defense + 100))
        self.health = max(0, self.health - finalDamage)

        return finalDamage

    # Represent's entity when printed out
    @override
    def __repr__(self):
        return f"{self.name} - Health: {self.health} | ATK: {self.attack} | DEF: {self.defense}"

    # Function for identifying the entity's class
    @abstractmethod
    def getType(self):
        pass
