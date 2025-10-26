import random
import string

def generate_password(length=12):
    """Generate a random password with given length."""
    if length < 4:
        return "Password length should be at least 4 characters."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("🔐 Password Generator")
    try:
        length = int(input("Enter password length (minimum 4): "))
        password = generate_password(length)
        print(f"\nYour generated password is: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
