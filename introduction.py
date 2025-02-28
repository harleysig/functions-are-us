
#1. Display an introduction to the game explaining rules and prompt for their name and display that in the welcome message.
#  Return the name to the main program and store it in variable so it can be used throughout the program.

def welcome(): 
    # Welcome user
    print( "Welcome to the game simulator")
    # Get their name
    sName = input("What is your name? ")
    # Display instructions using their name
    print("\n" + sName + " here are the instructions for the game simulator.\nFirst select your team. Then select the teams you want to play against.\nYou can play agaisnt as many teams as you'd like.\n")
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

# Assign their name to a vairiable


def main() : #Main function to call all other functions
    sPlayerName = welcome()
    teams = {}

    while True: 
        choice = menu()
        if choice == "1" : 
        elif choice == "2" : 
        elif choice == "3" : 
            print(f'Thanks for playing! Goodbye {sPlayerName.capitalize()}!')
        else :
            print(f'Invalid entry. Please try again.')

main()
