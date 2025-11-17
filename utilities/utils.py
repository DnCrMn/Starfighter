# Script that holds utility functions
import time

# Returns an integer of a choice given the prompt, the minimum, and the maximum value 
def getIntChoice(prompt, minValue, maxValue):
    while True:
        choice = slowInput(prompt)
        
        if choice.isdigit():
            num = int(choice)

            # If choice is within the min and max value
            if minValue <= num <= maxValue:
                return num

        # If input is invalid
        print(f"\nInvalid choice. Please enter a number between {minValue} and {maxValue}.")

# Gets the valid input given valid options
def getValidInput(prompt, validOptions):
    while True:
        choice = slowInput(prompt).strip().lower()

        # Return if choice is valid
        if choice in validOptions:
            return choice

        # Error message
        print(f"\nInvalid choice. Valid options: {', '.join(validOptions)}")

# Formats the printing of an item
def formatItem(item):
    return f"{item["name"]}: {item["description"]}" 

# Creates a slow typing effect for text printing given the text and delay
def slowPrint(text, delay = 0.08, end = "\n", flush = True):
    for char in text:
        print(char, end = "", flush = flush)
        time.sleep(delay)
    print(end = end, flush = flush)

# Slow print effect but for inputs
def slowInput(prompt, delay = 0.08):
    for char in prompt:
        print(char, end = "", flush = True)
        time.sleep(delay)
    return input()

# Prints ascii line by line given the art
def printASCII(art):
    # Only print if art is a list
    if art:
        for line in art:
            slowPrint(line, 0.005)
