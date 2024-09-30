#Tpc tp2
print("Welcome to Snowgames")
print("We'll now play a guessing game")
u = input("Would you like to guess the number the computer chose? Choose 1. Choose a number yourself? Choose 2")

user = int(u)

if user == 1 :

    import random
    num = random.randint(1,100)
    guess = 0


    while guess != num :
    
        guess = int(input("What do you think is the number"))

        if guess < num : 
            print("The number is higher")
        elif guess > num  : 
            print("Then number is lower")
        else :
            print("You have guessed right")

elif user == 2 :
    print("Pick any number between 1 and 100")
    high = 100
    low = 1 
    guess = (high + low)//2

    answer = input("Was the number you choose " + str(guess) + ". Please answer with 'yes' or 'no'")
    while answer == ("no") :
        hint = input("Was my guess 'too high' or 'too low'?")

        if hint == ("too high") :
            high = guess
            guess = (high + low)//2
        elif hint == ("too low") :
            low = guess
            guess = (high + low)//2

        answer = input("Was the number you choose " + str(guess) + ". Please answer with 'yes' or 'no'")
        print("That was fun, please come play again soon")