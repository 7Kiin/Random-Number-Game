import random


def guess_the_random_number(x):

    print("************************************")
    print("You need to guess the random number.")
    print("************************************")

    randomNumber = random.randint(1, x)

    userPrediction = 0

    while userPrediction != randomNumber:

        userPrediction = int(input(f"Guess the random number between 1 and {x}: "))
        
        if userPrediction < randomNumber:
            print("Wrong, you need a bigger one.")
        elif userPrediction > randomNumber:
            print("Wrong, you need a smaller one.")
        
    print(F"You are wright! {randomNumber} is the one.")


guess_the_random_number(10)