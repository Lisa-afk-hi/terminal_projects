import random

def get_level_settings():
    print("Choose difficulty level:")
    print("1. Easy (1-10, 5 attempts)")
    print("2. Medium (1-50, 7 attempts)")
    print("3. Hard (1-100, 10 attempts)")
    
    while True:
        choice = input("Enter 1, 2, or 3: ")
        if choice == '1':
            return 1, 10, 5
        elif choice == '2':
            return 1, 50, 7
        elif choice == '3':
            return 1, 100, 10
        else:
            print("Invalid choice. Please try again.")

def play_game():
    low, high, attempts = get_level_settings()
    secret_number = random.randint(low, high)
    
    print(f"\nI've picked a number between {low} and {high}.")
    print(f"You have {attempts} attempts to guess it!\n")
    
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if guess < secret_number:
            print("Too low!")
        elif guess > secret_number:
            print("Too high!")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempt} attempts!")
            break
    else:
        print(f"😞 Sorry, you ran out of attempts. The number was {secret_number}.")

def main():
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").lower()
        if again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()
