
#1. Display an introduction to the game explaining rules and prompt for their name and display that in the welcome message.
#  Return the name to the main program and store it in variable so it can be used throughout the program.
import random

def welcome(): 
    # Welcome user
    print( "Welcome to the game simulator")
    # Get their name
    sName = input("What is your name? ")
    # Display instructions using their name
    print("\nHello " + sName + ", here are the instructions for the game simulator.\nFirst select your team. Then select the teams you want to play against.\nYou can play agaisnt as many teams as you'd like.\n")
    return sName

def menu():
    while True: 
        print("""
        1. Start Over
        2. Select Home Team
        3. Quit
        """)
        choice = input("Select an option: ")
        if not choice in "123":
            print("Please enter 1, 2, or 3")
        else:
            return choice
          
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


def calc_score(home_team, away_team):
    home_score = 0
    opp_score = 0
    while home_score == opp_score:
        home_score = random.randrange(0,10)
        opp_score = random.randrange(0,10)

    if home_score > opp_score:
        outcome = "W"
    else:
        outcome = "L"
    
    print(f"{home_team} scored {home_score}. {away_team} scored {opp_score}.")
    return outcome


# Assign their name to a vairiable

teamSelect()


def main() : #Main function to call all other functions
    sPlayerName = welcome()
    teams = {}

    while True: 
        choice = menu()
        if choice == "1" : 
          print("placeholder")
        elif choice == "2" : 
            home_team=teamSelect()
            away_team=teamSelect()
            calc_score(home_team,away_team)
        elif choice == "3" : 
            print(f'Thanks for playing! Goodbye {sPlayerName.capitalize()}!')
            break
        else :
            print(f'Invalid entry. Please try again.')

main()
