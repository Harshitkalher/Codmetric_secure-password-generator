import random
import string

def generate_password(length=12, use_special_chars=True):
    if length < 4:
        return "Password length must be at least 4"

    # Define character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation if use_special_chars else ""

    # Ensure at least one character from each category
    all_chars = lower + upper + digits + special
    password = (
        random.choice(lower) +
        random.choice(upper) +
        random.choice(digits) +
        (random.choice(special) if use_special_chars else "")
    )

    # Fill the rest of the password length
    password += "".join(random.choices(all_chars, k=length - len(password)))

    # Shuffle the password to avoid patterns
    password = "".join(random.sample(password, len(password)))

    return password

# Get user input
length = int(input("Enter password length: "))
use_special = input("Include special characters? (yes/no): ").strip().lower() == "yes"

# Generate and display the password
password = generate_password(length, use_special)
print("Generated Password:", password)
