import random

def play():
    options = ["rock", "paper", "scissors"]
    user = input("Enter your choice (rock, paper, scissors): ").lower()
    
    # validate input
    while user not in options:
        user = input("Invalid choice. Please enter rock, paper, or scissors: ").lower()
    
    computer = random.choice(options)
    print(f"\nYou chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("🎉 You win!")
    else:
        print("😢 You lose!")

if __name__ == "__main__":
    while True:
        play()
        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing! 👋")
            break
