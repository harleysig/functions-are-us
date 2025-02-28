
#1. Display an introduction to the game explaining rules and prompt for their name and display that in the welcome message.
#  Return the name to the main program and store it in variable so it can be used throughout the program.

def Welcome(): 
    # Welcome user
    print( "Welcome to the game simulator")
    # Get their name
    sName = input("What is your name? ")
    # Display instructions using their name
    print("\nHello " + sName + ", here are the instructions for the game simulator.\nFirst select your team. Then select the teams you want to play against.\nYou can play agaisnt as many teams as you'd like.\n")
    return sName

# set up list of teams, setup selection of home and opp teams
def teamSelect() :
    teams = ["BYU", "ASU", "USU", "UofU", "BSU", "WSU", "WVU"]
    index = 1

    for item in teams:
        print (f"{index}. {item}")
        index = index + 1

    selection = int(input("Select your home team number:\n"))
    homeTeam = teams[selection-1]
    teams.remove(homeTeam)
    print (homeTeam)



# Assign their name to a vairiable
sPlayerName = Welcome()

teamSelect()


