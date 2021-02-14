from os import system

import commandFunctions

stopBot = False
def main():
    clearScreen()

    while not stopBot:
        returnVal = executeCommand()
        clearScreen()
        if(returnVal == None):
            print("the command did not return any data", "\n")
        else:
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
    elif command == "i":
        returnVal = commandFunctions.saveMiningConfig()
    elif command == "p":
        returnVal = commandFunctions.printMiningConfig()
    elif command == "s":
        returnVal = commandFunctions.startBotLoop()
    else:
        returnVal = "error: invalid command"

    return returnVal
    
def printCommands():
    print("-" * 25)

    print("c: close the bot")
    print("o: open a mining config")
    print("i: save a mining config")
    print("p: display current miningconfig data")
    print("s: start the bot")

    print("-" * 25)


def clearScreen():
    system("cls")
    print()


if __name__ == "__main__":
    main()