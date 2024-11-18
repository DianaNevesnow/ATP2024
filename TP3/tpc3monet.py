
print("Welcome to the 21 matchstick game!!!")
print("First you have to choose what version you'll like to play.")
print("Version1 you, the player, play first and the computer second.")
print("And Version2 the computer plays first ad you second.")

option = input("To play in Version1, enter 1. To play in Version2, enter 2")

if option == 1:

matches = 21
while matches > 1:
    player = int(input("How many matches do you want to take? Choose between 1 and 4 matches: "))
    print(f"You took {player} matches. {matches - player} matches remaining.")
    matches = matches - player
    comp = 5 - player
    print(f"The computer took {comp} matches. {matches - comp} matches remaining.")
    matches = matches - comp
print("You lost. It's your turn, and only 1 match is left.")     


elif option == 2:
   
matches = 21
while matches > 1:
    from random import randint
    comp = randint(1, 4)
    print(f"I took {comp} matches, {matches - comp} matches remain.")
    matches =  matches - comp
    player = int(input("Now it's your turn, how many matches do you want to take? "))
    print(f"You took {player} matches. Now {matches - player} matches remain.")

    matches =  matches - player
    if player + comp != 5:
        comp = 5 - player
        print(f"The computer took {comp} matches. {matches - comp} matches remain.")
        matches =  matches - comp
        player = int(input("Now it's your turn, how many matches do you want to take? "))
        print(f"You took {player} matches. Now {matches - player} matches remain.")
        matches =  matches - player
        while matches > 1:
            comp = 5 - player
            print(f"The computer took {comp} matches. {matches - comp} matches remain.")
            matches =  matches - comp
            player = int(input("Now it's your turn, how many matches do you want to take? "))
            print(f"You took {player} matches. Now {matches - player} matches remain.")
            matches =  matches - player
print("You lost. It's your turn, and only 1 match is left.")

else: 
   print("Invalid")