import random

while True:
    #Initialize the game variables
    while True:
        top_of_range = input("Type Highest Value: ")

        if top_of_range.isdigit():
            top_of_range = int(top_of_range)

            if top_of_range <= 0:
                print("Please type a number larger than 0.")
                continue
            else:
                break
        else:
            print("Please type a number")
            continue        

    random_number = random.randint(0, top_of_range)
    guesses = 0 

    while True:
        guesses += 1
        user_guess = input("Make A Guess. ")

        if user_guess.isdigit():
            user_guess = int(user_guess)
            if user_guess < 0 or user_guess > top_of_range:
                print(f"Please guess a number between 0 and {top_of_range}.")
                continue

        else:
            print("Please type a number.")
            continue

        if user_guess == random_number:
            print("Correct")
            break
        elif user_guess > random_number:
            print("Lower!")
        else:
            print("Higher!")
    print("You got it correct in", guesses, "Guesses!")        

    play_again = input("Do you want to play again (yes/no): ").lower()
    if play_again != "yes":
        break            

