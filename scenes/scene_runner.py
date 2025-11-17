# Script for running different paths for the game
import random
import json
from systems.encounters import triggerRandomEncounter
from utilities.utils import getIntChoice, slowPrint, printASCII

MIN_ENCOUNTERS_BEFORE_BOSS = 10 # Minimum encounters before you get to the boss.
MAX_ENCOUNTERS_BEFORE_BOSS = 15 # Maximum encounters before you get to the boss.

def runPath(player, pathsFile="data/paths.json"):
    with open(pathsFile) as f:
        paths = json.load(f)

    current = "prologue"
    encountersDone = 0 # Encounters done. Could be both item or combat encounter.

    while True:
        scene = paths[current] # Get the current path of the player

        # Print ascii art of the scene
        print()
        printASCII(scene.get("ascii"))

        # Print scene description
        desc = scene["description"]

        if scene.get("encounter_type") == "boss":
            # Only encounter boss if you have reached the minimum amount of encounters
            if encountersDone < MIN_ENCOUNTERS_BEFORE_BOSS:
                slowPrint("You sense something VERY DANGEROUS ahead. You feel unprepared, so you go to a different path", 0.03)

                # Grab any scene that is not a boss type
                detour = [key for key in paths if key != "boss_gate"]
                current = random.choice(detour) 

                continue # Skip to the next loop and go to a random path

            print()
            # If descriptions is a list, print each line
            if isinstance(desc, list):
                for line in desc:
                    slowPrint(line)
            else:
                slowPrint(desc)

            survived = triggerRandomEncounter(player, final = True) 

            if survived:
                slowPrint("YOU WIN! The boss has been defeated! The evil that was terrorizing the universe is no more!")

            break # Stop looping after the boss whether you win or not
        
        print()
        # If descriptions is a list, print each line
        if isinstance(desc, list):
            for line in desc:
                slowPrint(line)
        else:
            slowPrint(desc)

        print(f"\nEnemy Encounters Done: {encountersDone}")

        # --- Encounter handling ---
        if scene.get("encounter_type") == "random":
            survived = triggerRandomEncounter(player) 
            encountersDone += 1

            # Game over 
            if not survived:
                print("GAME OVER")
                break


        # --- Branching choices ---
        if "choices" in scene:
            options = list(scene["choices"].keys()) # Get the list of keys for the choices

            # List all options
            for i, opt in enumerate(options, 1):
                slowPrint(f"{i}) {opt}")

            # Handle player input
            choice = getIntChoice("\nChoose your path:\n> ", 1, len(options))
            current = scene["choices"][options[choice - 1]]
            continue # Skip next randomization

        # If there's no branching choices, pick the next scene randomly
        if "next" in scene:
            nextOptions = scene["next"]

            # If boss is unlocked and the next path leads to boss, force it when you exceed the max encounters
            if encountersDone >= MAX_ENCOUNTERS_BEFORE_BOSS:
                bossNext = [option for option in nextOptions if paths[option].get("encounter_type") == "boss"]

                # If boss next is not empty
                if bossNext:
                    current = bossNext[0]  # Force next scene to boss
                    continue

            # Otherwise, pick random next scene
            current = random.choice(nextOptions)
        else:
            return True
