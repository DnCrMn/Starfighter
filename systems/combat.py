# Has function for the game's combat
import random

from utilities.utils import (
    printASCII,
    getValidInput,
    getIntChoice, 
    slowPrint, 
    slowInput
)

from utilities.combat_log import (
    printBoxedASCII,
    logStats, 
    logAttack,
    logEnemyAttack,
    logFlee,
    logInventory,
    logItem, 
    logItemFail, 
    logVictory,
    logPlayerDefeated
)

# Valid actions for combat
validActions = {
    "attack": lambda player, enemy: attack(player, enemy),
    "flee": lambda player, enemy: flee(enemy),
    "item": lambda player, enemy: useItem(player)
}

# Engages combat with an enemy. Has the choice of attacking, fleeing, or using
# an item
def engageCombat(player, enemy):
    slowPrint(f"\nA hostile {enemy.name} appears!", 0.05)


    # Do not stop combat until the player or the enemy is not alive 
    while player.isAlive() and enemy.isAlive():
        print()
        # Print ascii art of enemy
        printASCII(enemy.ascii)

        # --- Stat Lines --- #
        logStats(player.ship, enemy)

        # --- Player's Turn --- #
        action = getValidInput(
            "\nDo you want to (attack), (flee), or use an (item)?\n> ",
            validActions.keys()
        )

        # Execute the player's chosen action
        result = validActions[action](player, enemy) # Returns a boolean to check if the combat should end

        slowInput("\n[Press ENTER to continue]", 0.05)

        # Output player death and return
        if not player.isAlive():
            logPlayerDefeated()
            slowInput("\n[Press ENTER to continue]", 0.05)
            return True

        # If an enemy died from an attack or item, return true
        if not enemy.isAlive():
            logVictory(enemy.name)
            slowInput("\n[Press ENTER to continue]", 0.05)
            return True

        # Skip loop if the action's result is retry
        if result == "retry":
            continue

        # # Stop combat if an action ends it
        if result is True:
            return player.isAlive()

        # --- Enemy's Turn --- #
        damageTaken = player.takeDamage(enemy.attack)
        logEnemyAttack(enemy.name, damageTaken)

        slowInput("\n[Press ENTER to continue]", 0.05)

    # Return whether the player survives or not
    return player.isAlive() 

# Function for attacking the enemy
# Returns true if attack ends combat
def attack(player, enemy):
    damage = enemy.takeDamage(player.ship.attack)
    logAttack(player.name, enemy.name, damage)

    # End combat if enemy dies
    return not enemy.isAlive()

# Function for fleeing
def flee(enemy):
    # If player cannot flee
    if enemy.fleeChance == 0:
        printBoxedASCII(
            "CANNOT FLEE",
            [f"You cannot escape from the {enemy.name}"]
        )
        return False

    # Roll for flee chance
    roll = random.randint(1, 100)
    if roll > enemy.fleeChance:
        printBoxedASCII(
            "ESCAPE FAILED",
            [f"You tried to flee, but the {enemy.name} blocks your way!"]
        )
        return False

    # If fleeing is successful
    logFlee()
    return True # You end the combat

# Function for using items
def useItem(player):
    # If player has no items
    if not player.inventory:
        print("You have no items!")
        return "retry"

    # Print list of items
    logInventory(player)
    
    # Get choice from player
    choice = getIntChoice("\nChoose an item number (press 0 to go back):\n> ", 0, len(player.inventory))

    # Go back to main actions
    if choice == 0:
        return "retry"

    # Get item and check if it is used successfully
    itemName = player.inventory[choice - 1]

    logItem(itemName)
    usedSuccessfully = player.useItem(itemName)

    # Print item feedback for player if it's unsuccessful
    if not usedSuccessfully:
        logItemFail(itemName)
        return "retry"

    return False
