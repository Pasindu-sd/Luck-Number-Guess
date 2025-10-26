import random

print("---Welcome to the Luck Guess Number Game!---")

while True:
    secret_number = random.randint(1,10)
    attempts = 0
    max_attempts = 3

    print("\nI'm thinking of a number between 1 and 10...")
    print(f"You have {max_attempts} attempts. Good Luck!")

    while attempts < max_attempts:
        guess = int(input("Enter Your guess: "))
        attempts +=1
        
        if guess == secret_number:
            print(f"Correct! You guessed the number in {attempts} attempts!")
            break       
        elif guess < secret_number:
            print("Too Low! Try Again...") 
        else:
            print("Too High! Try Again...")


    play_again = input("\nDo you want to play gain? (y/n): ").lower()
    if play_again != 'y':
        print("Thanks for playing! GoodBye!")
        break

    

      
