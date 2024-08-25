import random

youDict = {"r": 1, "p": -1, "s": 0}
reverseDict = {1: "Rock", -1: "Paper", 0: "Scissors"}

while True:
    computer = random.choice([0, -1, 1])

    youstr = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ").strip().lower()
    
    # Check if the input is valid
    if youstr not in youDict:
        print("Invalid choice! Please choose from (r, p, s).")
        continue

    you = youDict[youstr]

    print(f"\nYou chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if you == computer:
        print("It's a Draw!")
    else:
        if (you == 1 and computer == 0) or (you == 0 and computer == -1) or (you == -1 and computer == 1):
            print("You win!")
        else:
            print("You lost!")

    # Ask the user if they want to play again
    play_again = input("\nDo you want to play again? (y/n): ").strip().lower()
    if play_again != 'y':
        print("Thanks for playing!")
        break
