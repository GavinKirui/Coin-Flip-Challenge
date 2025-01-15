import random

head=1
tail=0
your_guess= int(input("Enter your guess: "))
print(f"Your guess is {your_guess}")
computer_guess= random.randint(0,1)
print(f"computer_guess is {computer_guess}")
if computer_guess==your_guess:
    print("You Win!")
else:
    print("You lose!")
        
    