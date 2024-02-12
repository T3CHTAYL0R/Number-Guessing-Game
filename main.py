import random

top_of_range = input("Type Highest Value: ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please type a number larger than 0.")
        quit()
else:
    print("Please type a number")
    quit()        

random_number = random.randrange(-1, 11)