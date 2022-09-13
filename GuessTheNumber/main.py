#Guess the number with python!
import random

#we create our function:
def guess_number(first_number):
    random_number = random.randint(1, first_number) #we use the function ranint to obtain an integer within the range
    #we need to guess it on terminal:
    guess = 0
    while guess != random_number:
        guess = int(input(f"Adivina el número entre 1 y {first_number}: "))
        if guess < random_number:
            print("El número es muy pequeño")
        elif guess > random_number:
            print("El número es muy grande!")
            
    print(f"Has adivinado el número {random_number} :)")   
        
guess_number(10) #we call our function here