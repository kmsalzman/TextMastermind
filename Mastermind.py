# File Name:   Mastermind.py
# Purpose:     The computer generates a random color pattern and gives hints on how close the user is to guessing the correct pattern
# Author:      Kyle Salzman
# Date:        January 15, 2021
 
#Import random module
import random

#Declare Global Variables
colorList = ["blue", "red", "white", "green", "yellow", "purple"]
blackPeg = 0
turnNum = 0

#Generate a seed based on the seed value of 350

#generateSecretCode function take a list of colors as input and returns a list of 4 colors randomly generated based on the seed input.
def generateSecretCode(colorList):
    #Create the computer's list of colors, computerList
    computerList = []
    
    #Generate a list of 4 random colors from the valid color list
    for num in range(4):
        randomValue = random.randint(0, 5)
        computerList.append(colorList[randomValue])
    return computerList

#computeExactMatches takes the computer's list of colors and the player's list of colors as input and returns the number of correct colors in the correct position
def computeExactMatches(computerColorList, playerColorList):
    #Declare local variables
    black = 0
    white = 0
    
    #Loop through list of colors
    for indexPos in range(4):
        #If color in computerColorList and playerColorList are the same at the same index position, replace color with solved and add 1 to the variable black to track exact matches
        if computerColorList[indexPos] == playerColorList[indexPos]:
            #computerColorList[indexPos] = "Solved"
            black += 1
    
    #Return the variables black and white
    return black

#computePartialMatches takes the computer's list of colors and the player's list of colors as input and returns the number of correct colors in the incorrect positions
def computePartialMatches(computerColorList, playerColorList):
    #Declare Local Variable
    white = 0
    
    #Loop through player's color list, playerColorList
    for indexPos in range(4):
        currentColor = playerColorList[indexPos]
        #If the color is in the computer's colorList, computerColorList, and is not at the same index as the player's color list, playerColorList, then add 1 to the variable white to track the number of partial matches
        if currentColor in computerColorList and playerColorList[indexPos] != computerColorList[indexPos]:
            white += 1
    
    #Return the variable white
    return white
        
if __name__ == "__main__":

    #Starts the game
    print("Mastermind Game")
    print("The computer has generated a secret color code.")
    print("Can you guess the code?")
    print("These are the valid colors you can use:", end = "")
    
    #Lists the valid colors that can be used
    for colors in colorList:
        print(" " + colors, end = "")
    print("\n")
    
    #Generates the computer's color list from the seed generated and stores it in the computerColorList variable    
    computerColorList = generateSecretCode(colorList)
    
    #Loops as long as the player has not guessed all the colors in the correct spots
    while blackPeg < 4:
        #Tracks the turn number the player is on
        turnNum += 1
        
        #Creates an empty color list for the player
        playerColorList = []
        
        #Loops as long as the player has not entered 4 valid colors
        while len(playerColorList) != 4:
            #Takes a color as input
            colorGuess = input("Please enter color " + str(len(playerColorList) + 1) + " : ")
            
            #If the color entered is in the list of valid colors it is added to the player's list of colors, playerColorList
            if colorGuess.lower() in colorList:
                playerColorList.append(colorGuess.lower())
            #Gives an error if the color entered is not within the list of valid colors, colorList
            else:
                print("That is not a valid color. Try again.")
        
        #Gets the number of exact matches and partial matches. Stores them in the blackPeg and whitePeg variables
        blackPeg = computeExactMatches(computerColorList, playerColorList)
        
        #Run the function computePartialMatches and store answer in the variable white
        whitePeg = computePartialMatches(computerColorList, playerColorList)
        
        #Shows user how many exact and partial matches they got
        print(blackPeg, "black")
        print(whitePeg, "white\n\n")
    
    #Prints congratulations message if user got 4 exact matches and says how many turns it took.    
    print("Congratulations, you guessed the secret code!")
    print("It took you", turnNum, "turn(s).")