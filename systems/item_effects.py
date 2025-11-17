# Holds dictionary for value effects and its corresponding functions
from utilities.utils import slowPrint

itemEffects = {
    # Dictionary uses lambda to map keys with functions
    "heal": lambda player, value: heal(player, value),
    "attack": lambda player, value: increaseATK(player, value),
    "defense": lambda player, value: increaseDEF(player, value),
}

# Heals the player based on the value given
def heal(player, value):
    # Clamp health when healing player
    player.ship.health = min(player.ship.maxHealth, player.ship.health + value)
    slowPrint(f"\n[The {player.ship.name} restored {value} HP!]")

# Increases the player's attack based on the value given
def increaseATK(player, value):
    player.ship.attack += value
    slowPrint(f"\n[{player.ship.name}'s ATK is increased by {value}!]")

# Increases the player's defense based on the value given
def increaseDEF(player, value):
    player.ship.defense += value
    slowPrint(f"\n[The {player.ship.name} fortifies its DEF by {value}!]")
