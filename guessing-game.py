# CMPT 120L 113
# Derek Francisco
# 20 Sep 2018
###

def main():
    print("PYTHON GUESSING GAME")

def animal(bear):
    animal = "bear"
    return animal

print("Thinking of an animal")
while True:
    guess = input("Guess the name of the animal ")
    if guess == "bear":
        print("You are right!")
        break

    else:
        print("Sorry that is not correct, try again. ")
        

