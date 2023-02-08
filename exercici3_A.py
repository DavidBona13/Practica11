import random as R

#Numero secreto, peta si no le pones nada, te ayuda a adivinar el numero indicandote si es mayor o menor
def SecretNumber():
    SecretNumber = R.randint(0,100)
    IsTheNumber = False
    while not IsTheNumber:
        ChoosenNumber = input("Choose a number between 0 and 100!\n")
        if int(ChoosenNumber) == SecretNumber:
            IsTheNumber = True
            print("Good job, the number is {}".format(SecretNumber))
            return ChoosenNumber
        else:
            if int(ChoosenNumber) > SecretNumber: print("{} is bigger than the secret number!".format(ChoosenNumber))
            else: print("{} is lower than the secret number!".format(ChoosenNumber))
