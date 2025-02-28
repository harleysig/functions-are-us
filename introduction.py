# Harley Sigmon, Will Robison, Paris Ward, Christian Yoder, Hunter Johanson
# This program allows users to choose teams and tracks their records. The user can search for any team's final record.

import random

# This function welcomes the user and prompts for a name
def welcome() : 
    # Welcome user
    print( "Welcome to the game simulator")
    # Get their name
    sName = input("What is your name? ")
    # Display instructions using their name
    print("\nHello " + sName + ", here are the instructions for the game simulator.\nFirst select your team. Then select the teams you want to play against.\nYou can play agaisnt as many teams as you'd like.\n")
    return sName

# Displays menu and returns choice
def menu() :
    while True: 
        print("""
        1. Select Team & Play Game
        2. Search Records
        3. Quit
        """)
        choice = input("Select an option: ")

        return choice

# Creates team list and allows user to select home and away team (default is BYU)
def team(t=1,home_team="BYU") :
    teams = ["BYU", "ASU", "USU", "UofU", "BSU", "WSU", "WVU"]
    if t == "op":
        # removes home team from list of opponent teams
        teams.remove(home_team)

    index = 1

    for item in teams:
        print (f"{index}. {item}")
        index += 1
    while True :
        choiceTeam = int(input("\nWhich team would you like to select (choose a number)? "))-1
        if choiceTeam > 6 or choiceTeam < 0 :
            print ("Invalid choice. Select a number between 1 and 7.\n")
        else:
            return teams[choiceTeam]

# Takes home and away team and generates random scores. Returns W or L for each team
def play(home_team,away_team,team_dict) :
    homeScore = random.randint(0,11)
    opScore = random.randint(0,11)
    
    print(f'\nGame Results: {home_team} {homeScore} - {away_team} {opScore}')
    if homeScore > opScore : 
        print(f'{home_team} wins!\n')
        team_dict[home_team].append("W")
        team_dict[away_team].append("L")
    else : 
        print(f'{away_team} wins!\n')
        team_dict[home_team].append("L")
        team_dict[away_team].append("W")

# User searches for a team and displays final record
def record(team_dict) : 
    teamChoice = input("\nEnter Your Home Team Name: ").upper()
    if teamChoice in team_dict : 
        print(f'\n{teamChoice} Season Results: {team_dict[teamChoice].count("W")} Wins - {team_dict[teamChoice].count("L")} Losses.\n')
    else : 
        print(f'\n{teamChoice} is not in the list. Please try again.\n')


def main() : 
    playName = welcome()
    team_dict = {"BYU" : [], "ASU" : [], "USU" : [], "UofU" : [], "BSU" : [], "WSU" : [], "WVU" : []}
    
    # Loops until user selects quit. Allows user to run as many games as they want
    while True: 
        choice = menu()
        if choice == "1" : 
            home_team = team()
            away_team = team("op",home_team)
            play(home_team,away_team,team_dict)
        elif choice == "2" : 
            record(team_dict)
        elif choice == "3" : 
            print(f'Thanks for playing! Goodbye {playName.capitalize()}!')
            break
        else :
            print(f'Invalid entry. Please try again.')


main()
