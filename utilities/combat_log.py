# Utility functions for printing ascii art of the combat
from collections import Counter
from utilities.utils import formatItem, slowPrint

# Generates an ascii health bar art 
def generateHealthBar(hp, maxHP, barLength = 20):
    # Reserve space for "HP: X/Y " part
    hpText = f"{hp}/{maxHP}"
    barWidth = barLength - len("HP: ") - len(hpText) - 1  # -1 for space between bar and text

    ratio = max(hp, 0) / maxHP # Get the ratio for the bar fill
    filled = int(ratio * barWidth) # Represent the bar fill using an integer

    empty = barWidth - filled # Calculate the empty space for the the bar
    bar = f"[{'█' * filled}{'-' * empty}]" # Format bar ascii art 

    return f"HP: {bar} {hpText}"

# Turns an entity into a list of formatted string containing stats
def formatStats(entity):
    return [
        f"Name: {entity.name}",
        generateHealthBar(entity.health, entity.maxHealth),
        f"ATK: {entity.attack}",
        f"DEF: {entity.defense}"
    ]

def logStats(player, enemy):
    # Format stat lines for player and enemy
    playerLines = formatStats(player)
    enemyLines = formatStats(enemy)

    # Ensure equal number of lines for the player and enemy stats
    maxLines = max(len(playerLines), len(enemyLines))

    # Add padding if necessary
    playerLines += [""] * (maxLines - len(playerLines))
    enemyLines += [""] * (maxLines - len(enemyLines))

    # Merge formatted lines of player and enemy
    mergedLines = [
        f"{p.ljust(22)}    ||    {e}"
        for p, e in zip(playerLines, enemyLines)
    ]

    printBoxedASCII("STATUS REPORT", mergedLines)

# Prints a boxed ascii message
def printBoxedASCII(title, lines):
    # --- Box Formatting --- #
    # Get the max length between the title and all of the lines inside the box
    width = max(len(title), *(len(l) for l in lines)) + 10 
    top = "╔" + "═" * width + "╗" # Top part of the box
    bottom = "╚" + "═" * width + "╝" # Bottom part of the box
    titleLine = f"║  {title.center(width-4)}  ║" # Title of the box

    printSpeed = 0.01 
    # Print the box with its contents 
    slowPrint("\n" + top, printSpeed)
    slowPrint(titleLine, printSpeed)
    slowPrint("╠" + "═" * width + "╣", printSpeed)

    # Print the lines inside the box
    for line in lines:
        slowPrint(f"║  {line.ljust(width-4)}  ║", printSpeed)

    slowPrint(bottom, printSpeed)

# Prints the attack using a formatted ascii box
def logAttack(attacker, target, damage):
    printBoxedASCII(
        "ATTACK!",
        [
            f"{attacker} strikes {target}!",
            f"Damage dealt: {damage}"
        ]
    )

# Prints the enemies attack using a formatted ascii box
def logEnemyAttack(enemyName, damage):
    printBoxedASCII(
        "ENEMY TURN",
        [
            f"{enemyName} attacks you!",
            f"Damage taken: {damage}"
        ]
    )

# Logs the player's inventory using a formatted ascii box
def logInventory(player):
    # Count item dupes using its name
    itemCount = Counter(item["name"] for item in player.inventory)

    # Convert inventory into lines with quanitites
    lines = []
    for index, (name, count) in enumerate(itemCount.items(), start=1):
        # Find the first occurrence of this item to get the description
        item = next(item for item in player.inventory if item["name"] == name)
        line = f"{index}) {name} (x{count}) - {item['description']}"
        lines.append(line) # Add item to the line

    printBoxedASCII(
        f"CADET LIEUTENANT {player.name}'s Items:",
        lines
    )

# Logs item that is used using a formatted ascii box
def logItem(itemName):
    printBoxedASCII(
        "ITEM USED",
        [f"You used {itemName["name"]}!"]
    )

# Logs item fail using a formatted ascii box
def logItemFail(reason):
    printBoxedASCII(
        "ITEM FAILED",
        [reason]
    )

# Logs when the player flees using a formatted ascii box
def logFlee():
    printBoxedASCII(
        "FLEE SUCCESS",
        ["You successfully escaped combat.", "You live to fight another day."]
    )

# Logs victory screen using a formatted ascii box
def logVictory(enemyName):
    printBoxedASCII(
        "VICTORY!",
        [f"{enemyName} has been defeated!"]
    )


# Logs lose screen using a formatted ascii box
def logPlayerDefeated():
    printBoxedASCII(
        "YOU DIED",
        [
            "Your ship can no longer fight.", 
            "With all of the sustained damage your ship received, it can no longer hold itself.",
            "Your ship explodes, leaving no trace of you."
        ]
    )
