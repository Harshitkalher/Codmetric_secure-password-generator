import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    # Create a pool of characters based on user preferences
    character_pool = ''
    
    if use_uppercase:
        character_pool += string.ascii_uppercase
    if use_lowercase:
        character_pool += string.ascii_lowercase
    if use_digits:
        character_pool += string.digits
    if use_special:
        character_pool += string.punctuation

    # Ensure that the character pool is not empty
    if not character_pool:
        raise ValueError("At least one character type must be selected.")

    # Generate a random password
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Secure Password Generator!")
    
    # Get user input for password length and character types
    length = int(input("Enter the desired password length (minimum 4): "))
    if length < 4:
        print("Password length should be at least 4.")
        return

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    # Generate the password
    password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
    
    # Display the generated password
    print(f"Generated Password: {password}")

    # Optionally copy the password to clipboard (requires pyperclip)
    copy_to_clipboard = input("Do you want to copy the password to clipboard? (y/n): ").lower() == 'y'
    if copy_to_clipboard:
        try:
            import pyperclip
            pyperclip.copy(password)
            print("Password copied to clipboard!")
        except ImportError:
            print("pyperclip module is not installed. Install it using 'pip install pyperclip' to enable clipboard functionality.")

if __name__ == "__main__":
    main()