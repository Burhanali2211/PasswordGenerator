import random
from datetime import datetime

# Menu Function


def show_menu():
    print("Welcome to the Password Generator!")
    print("1. Generate a New Password")
    print("2. View Saved Passwords")
    print("3. Exit")

# Get Password Length


def get_password_length():
    while True:
        try:
            password_length = int(input("Enter password length (minimum 4): "))
            if password_length >= 4:
                return password_length
            else:
                print("Password length must be at least 4!")
        except ValueError:
            print("Invalid input! Please enter a number.")

# Get User Preferences


def get_character_preferences():
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    include_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    if not (include_uppercase or include_lowercase or include_numbers or include_special_chars):
        print("You must select at least one character type!")
        return get_character_preferences()

    return include_uppercase, include_lowercase, include_numbers, include_special_chars

# Build Character Pool


def create_character(include_uppercase, include_lowercase, include_numbers, include_special_chars):
    character = ""
    if include_uppercase:
        character += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if include_lowercase:
        character += "abcdefghijklmnopqrstuvwxyz"
    if include_numbers:
        character += "0123456789"
    if include_special_chars:
        character += "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
    return character

# Generate Password


def generate_password(password_length, character):
    generated_password = ''.join(random.choice(character)
                                for _ in range(password_length))
    return generated_password

# Save Password to File


def save_password_to_file(password_description, generated_password):
    with open("passwords.txt", "a") as file:
        file.write(
            f"{datetime.now()} - {password_description}: {generated_password}\n")
    print("Password saved successfully!")

# View Saved Passwords


def show_saved_passwords():
    try:
        with open("passwords.txt", "r") as file:
            print("\nSaved Passwords:")
            print(file.read())
    except FileNotFoundError:
        print("No saved passwords found!")


# Main Program
while True:
    show_menu()
    user_choice = input("Enter your choice (1/2/3): ")

    if user_choice == '1':
        password_length = get_password_length()
        include_uppercase, include_lowercase, include_numbers, include_special_chars = get_character_preferences()
        character = create_character(
            include_uppercase, include_lowercase, include_numbers, include_special_chars)

        if character:
            generated_password = generate_password(
                password_length, character)
            print(f"\nGenerated Password: {generated_password}")

            save_option = input(
                "Do you want to save this password? (y/n): ").lower()
            if save_option == 'y':
                password_description = input("Enter a description for this password (e.g., 'Email Account'):")
                save_password_to_file(password_description, generated_password)
        else:
            print("Character pool is empty. Restart and select at least one option.")

    elif user_choice == '2':
        show_saved_passwords()

    elif user_choice == '3':
        print("Goodbye!")
        break

    else:
        print("Invalid choice! Please select 1, 2, or 3.")
