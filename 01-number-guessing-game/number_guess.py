# number_guess.py
import random

def choose_difficulty():
    """Return difficulty 1 (easy), 2 (medium), or 3 (hard)."""
    print("Choose difficulty: (1) Easy (2) Medium (3) Hard")
    while True:
        choice = input("Enter 1 / 2 / 3: ").strip()
        if choice in ("1", "2", "3"):
            return int(choice)
        print("Invalid choice. Please enter 1, 2, or 3.")

def get_max_attempts(diff):
    """Return allowed attempts by difficulty."""
    return {1: 10, 2: 6, 3: 4}[diff]

def get_range_by_difficulty(diff):
    """Return the upper bound of the secret number based on difficulty."""
    return {1: 50, 2: 100, 3: 200}[diff]

def play_once():
    diff = choose_difficulty()
    max_attempts = get_max_attempts(diff)
    upper = get_range_by_difficulty(diff)
    secret = random.randint(1, upper)
    attempts = 0

    print(f"\nI have chosen a number between 1 and {upper}. You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        attempts += 1
        prompt = f"Attempt {attempts}/{max_attempts} — Enter your guess (1-{upper}): "
        try:
            guess = int(input(prompt).strip())
        except ValueError:
            print("Please enter a valid integer.\n")
            attempts -= 1  # don't count invalid input
            continue

        if guess < 1 or guess > upper:
            print(f"Your guess must be between 1 and {upper}.\n")
            attempts -= 1
            continue

        if guess == secret:
            print(f"\n🎉 Correct! The number was {secret}. You took {attempts} attempts.\n")
            return True, attempts, diff
        elif guess < secret:
            print("Too low.\n")
        else:
            print("Too high.\n")

    print(f"💥 Out of attempts. The secret number was {secret}. Better luck next time!\n")
    return False, attempts, diff

def main():
    print("=== Number Guessing Game ===")
    while True:
        result = play_once()
        again = input("Play again? (y/N): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
