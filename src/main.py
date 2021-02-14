from os import system

import commandFunctions

stopBot = False
def main():
    clearScreen()

    while not stopBot:
        returnVal = executeCommand()
        clearScreen()
        print(returnVal, "\n")

    system("cls")

def executeCommand():
    global stopBot

    printCommands()

    command = input("command: ")

    command = command.replace(" ", "")
    command = command.lower()

    clearScreen()

    returnVal = None
    if command == "c":
        stopBot = True
    elif command == "o":
        returnVal = commandFunctions.loadMiningConfig()
    elif command == "p":
        returnVal = commandFunctions.saveMiningConfig()
    else:
        returnVal = "error: invalid command"

    return returnVal
    
def printCommands():
    print("-" * 25)

    print("c: close the bot")
    print("o: open a mining config")
    print("p: save a mining config")

    print("-" * 25)


def clearScreen():
    system("cls")
    print()


if __name__ == "__main__":
    main()